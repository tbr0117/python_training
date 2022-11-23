from pyodata.v2.service import *


class CustomService(Service):
    def __init__(self, url, schema, connection):
        self._url = url
        self._schema = schema
        self._connection = connection
        self._entity_container = CustomEntityContainer(self)
        self._function_container = FunctionContainer(self)

        self._config = {'http': {'update_method': 'PATCH'}}

    def create_batch(self, batch_id=None):
        """Create instance of OData batch request"""

        def batch_handler(batch, parts):
            """Process parsed multipart request (parts)"""

            logging.getLogger(LOGGER_NAME).debug(
                'Batch handler called for batch %s', batch.id)

            result = []
            for part, req in zip(parts, batch.requests):
                logging.getLogger(LOGGER_NAME).debug(
                    'Batch handler is processing part %s for request %s', part, req)

                # if part represents multiple requests, dont' parse body and
                # process parts by appropriate reuqest instance
                if isinstance(req, MultipartRequest):
                    result.append(req.handler(req, part))
                else:
                    # part represents single request, we have to parse
                    # content (without checking Content type for binary/http)
                    response = ODataHttpResponse.from_string(part[0])
                    result.append(req.handler(response))
            return result

        return BatchRequest(self._url, self._connection, batch_handler, batch_id)

    def create_changeset(self, changeset_id=None):
        """Create instance of OData changeset"""

        def changeset_handler(changeset, parts):
            """Gets changeset response from HTTP response"""

            logging.getLogger(LOGGER_NAME).debug(
                'Changeset handler called for changeset %s', changeset.id)

            result = []

            # check if changeset response consists of parts, this is important
            # to distinguish cases when server responds with single HTTP response
            # for whole request
            if not isinstance(parts[0], list):
                # raise error (even for successfull status codes) since such changeset response
                # always means something wrong happened on server
                response = ODataHttpResponse.from_string(parts[0])
                raise HttpError('Changeset cannot be processed due to single response received, status code: {}'.format(
                    response.status_code), response)

            for part, req in zip(parts, changeset.requests):
                logging.getLogger(LOGGER_NAME).debug('Changeset handler is processing part %s for request %s', part,
                                                     req)

                if isinstance(req, MultipartRequest):
                    raise PyODataException(
                        'Changeset cannot contain nested multipart content')

                # part represents single request, we have to parse
                # content (without checking Content type for binary/http)
                response = ODataHttpResponse.from_string(part[0])

                result.append(req.handler(response))

            return result

        return Changeset(self._url, self._connection, changeset_handler, changeset_id)


class CustomEntityContainer(EntityContainer):
    def __init__(self, service):
        self._service = service

        self._entity_sets = dict()

        for entity_set in self._service.schema.entity_sets:
            self._entity_sets[entity_set.name] = CustomEntitySetProxy(
                self._service, entity_set)


class CustomEntitySetProxy(EntitySetProxy):
    def get_entity(self, key=None, **args):
        """Get entity based on provided key properties"""

        def get_entity_handler(response):
            """Gets entity from HTTP response"""

            if response.status_code != HTTP_CODE_OK:
                raise HttpError('HTTP GET for Entity {0} failed with status code {1}'
                                .format(self._name, response.status_code), response)

            entity = response.json()['d']
            etag = response.headers.get('ETag', None)

            return _custom_prepare_response(self._service, self._entity_set, self._entity_set.entity_type, entity, etag=etag)

        if key is not None and isinstance(key, EntityKey):
            entity_key = key
        else:
            entity_key = EntityKey(self._entity_set.entity_type, key, **args)

        self._logger.info('Getting entity %s for key %s and args %s',
                          self._entity_set.entity_type.name, key, args)

        return EntityGetRequest(get_entity_handler, entity_key, self)

    def get_entities(self):
        """Get all entities"""
        def get_entities_handler(response):
            """Gets entity set from HTTP Response"""

            if response.status_code != HTTP_CODE_OK:
                raise HttpError('HTTP GET for Entity Set {0} failed with status code {1}'
                                .format(self._name, response.status_code), response)

            content = response.json()

            if isinstance(content, int):
                return content

            entities = content['d']
            total_count = None

            if isinstance(entities, dict):
                if '__count' in entities:
                    total_count = int(entities['__count'])
                entities = entities['results']

            self._logger.info('Fetched %d entities', len(entities))

            result = ListWithTotalCount(total_count)
            for props in entities:
                entity = _custom_prepare_response(
                    self._service, self._entity_set, self._entity_set.entity_type, props)
                result.append(entity)

            return result

        entity_set_name = self._alias if self._alias is not None else self._entity_set.name
        return GetEntitySetRequest(self._service.url, self._service.connection, get_entities_handler,
                                   self._parent_last_segment + entity_set_name, self._entity_set.entity_type)

    def create_entity(self, return_code=HTTP_CODE_CREATED):
        """Creates a new entity in the given entity-set."""

        def create_entity_handler(response):
            """Gets newly created entity encoded in HTTP Response"""

            if response.status_code != return_code:
                raise HttpError('HTTP POST for Entity Set {0} failed with status code {1}'
                                .format(self._name, response.status_code), response)

            entity_props = response.json()['d']
            etag = response.headers.get('ETag', None)

            return _custom_prepare_response(self._service, self._entity_set, self._entity_set.entity_type, entity_props, etag=etag)

        return EntityCreateRequest(self._service.url, self._service.connection, create_entity_handler, self._entity_set,
                                   self.last_segment)

    def update_entity(self, key=None, method=None, **kwargs):
        """Updates an existing entity in the given entity-set."""

        def update_entity_handler(response):
            """Gets modified entity encoded in HTTP Response"""

            if response.status_code != 204:
                raise HttpError('HTTP modify request for Entity Set {} failed with status code {}'
                                .format(self._name, response.status_code), response)

        if key is not None and isinstance(key, EntityKey):
            entity_key = key
        else:
            entity_key = EntityKey(self._entity_set.entity_type, key, **kwargs)

        self._logger.info('Updating entity %s for key %s and args %s',
                          self._entity_set.entity_type.name, key, kwargs)

        if method is None:
            method = self._service.config['http']['update_method']

        return EntityModifyRequest(self._service.url, self._service.connection, update_entity_handler, self._entity_set,
                                   entity_key, method=method)

    def delete_entity(self, key: EntityKey = None, **kwargs):
        """Delete the entity"""

        def delete_entity_handler(response):
            """Check if entity deletion was successful"""

            if response.status_code != 204:
                raise HttpError(f'HTTP POST for Entity delete {self._name} '
                                f'failed with status code {response.status_code}',
                                response)

        if key is not None and isinstance(key, EntityKey):
            entity_key = key
        else:
            entity_key = EntityKey(self._entity_set.entity_type, key, **kwargs)

        return EntityDeleteRequest(self._service.url, self._service.connection, delete_entity_handler, self._entity_set,
                                   entity_key)


def _custom_prepare_response(service, entity_set, entity_type, proprties=None, entity_key=None, etag=None):
    _custom = {
        "_logger": logging.getLogger(LOGGER_NAME),
        "_service": service,
        "_entity_set": entity_set,
        "_entity_type": entity_type,
        "_key_props": entity_type.key_proprties,
        "_cache": dict(),
        "_entity_key": entity_key,
        "_etag": etag
    }
    if proprties is not None:
        metadata = proprties.get('__metadata', dict())
        _custom['_etag_body'] = metadata.get('etag', None)
        if etag is not None and _custom['_etag_body'] is not None and _custom['_etag_body'] != etag:
            raise PyODataException(
                'Etag from header does not match the Etag from response body')

        if _custom['_etag_body'] is not None:
            _custom['_etag'] = _custom['_etag_body']

        # first, cache values of direct properties
        for type_proprty in _custom['_entity_type'].proprties():
            if type_proprty.name in proprties:
                if proprties[type_proprty.name] is not None:
                    _custom['_cache'][type_proprty.name] = type_proprty.from_json(
                        proprties[type_proprty.name])
                else:
                    # null value is in literal form for now, convert it to python representation
                    _custom['_cache'][type_proprty.name] = type_proprty.from_literal(
                        type_proprty.typ.null_value)

        # then, assign all navigation properties
        for prop in _custom['_entity_type'].nav_proprties:

            if prop.name in proprties:

                # entity type of navigation property
                prop_etype = prop.to_role.entity_type

                # cache value according to multiplicity
                if prop.to_role.multiplicity in \
                        [model.EndRole.MULTIPLICITY_ONE,
                            model.EndRole.MULTIPLICITY_ZERO_OR_ONE]:

                    # cache None in case we receive nothing (null) instead of entity data
                    if proprties[prop.name] is None:
                        _custom['_cache'][prop.name] = None
                    else:
                        _custom['_cache'][prop.name] = _custom_prepare_response(
                            service, None, prop_etype, proprties[prop.name])

                elif prop.to_role.multiplicity == model.EndRole.MULTIPLICITY_ZERO_OR_MORE:
                    # default value is empty array
                    _custom['_cache'][prop.name] = []

                    # if there are no entities available, received data consists of
                    # metadata properties only.
                    if 'results' in proprties[prop.name]:

                        # available entities are serialized in results array
                        for entity in proprties[prop.name]['results']:
                            _custom['_cache'][prop.name].append(
                                _custom_prepare_response(service, None, prop_etype, entity))
                else:
                    raise PyODataException('Unknown multiplicity {0} of association role {1}'
                                           .format(prop.to_role.multiplicity, prop.to_role.name))
        return {
            **_custom['_cache'],
            "__metadata": {
                "etag": _custom['_etag']
            }
        }
