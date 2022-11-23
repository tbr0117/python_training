
import requests

from .customOData import customClient
from requests.models import Response




class ServiceBase:
    def __init__(self, sServce_url, sClent):
        if not sServce_url or not sClent:
            return

        params = {"sap-client": sClent}
        self._service_url = sServce_url
        self._session = requests.session()
        self._session.params = params
        self.fetchCSRFToken()
        self._service_instance = customClient.CustomClient(
            sServce_url, self._session)

    def getEntitySet(self, sEntityName):
        return getattr(self._service_instance.entity_sets, sEntityName)

    def readEntitySet(self, oRequest={}):
        sEntityName = oRequest.get("entityName", "")
        if not sEntityName:
            return
        entity_set_request = self.getEntitySet(sEntityName).get_entities()

        sSelect = oRequest.get("select", "")
        sFilter = oRequest.get("filter", "")

        if sSelect:
            entity_set_request.select(sSelect)

        if sFilter:
            entity_set_request.filter(sFilter)

        entity_set_request.skip(oRequest.get("skip", 0))
        entity_set_request.top(oRequest.get("top", None))
        sCount = oRequest.get("count", None)
        if sCount == "inline":
            entity_set_request.count(inline=True)
        elif sCount:
            entity_set_request.count()

        result = entity_set_request.execute()

        # final_result = dict(count=len(result),
        #                     totalCount=result.total_count, data=[])
        # for r in result:
        #     record = dict(r._cache.items())
        #     final_result["data"].append(record)

        return result

    def readEntity(self, oRequest={}):
        read_request = self.prepareReadRequest(oRequest)
        if read_request is None:
            return
        oResponse = read_request.execute()
        print(oRequest)

    def createEntity(self, oRequest={}):
        create_request = self.prepareCreateRequest(oRequest)
        if create_request is None:
            return
        oResponse = create_request.execute()
        print(oResponse)

    def updateEntity(self, oRequest={}):
        update_request = self.prepareUpdateRequest(oRequest)
        if update_request is None:
            return
        oResponse = update_request.execute()
        print(oResponse)

    def deleteEntity(self, oRequest={}):
        delete_request = self.prepareDeleteRequest(oRequest)
        if delete_request is None:
            return
        oResponse = delete_request.execute()
        print(oResponse)

    def processBatch(self, oRequests={}):
        batch = self._service_instance.create_batch()
        if "read" is oRequests:
            for oReq in oRequests.read:
                request = self.prepareReadRequest(oReq)
                if not request is None:
                    batch.add_request(request)

        if "delete" is oRequests and oRequests.delete:
            changeset = self._service_instance.create_changeset()
            for oReq in oRequests.delete:
                request = self.prepareDeleteRequest(oReq)
                if not request is None:
                    changeset.add_request(request)
            batch.add_request(changeset)

        if "create" is oRequests and oRequests.create:
            changeset = self._service_instance.create_changeset()
            for oReq in oRequests.create:
                request = self.prepareCreateRequest(oReq)
                if not request is None:
                    changeset.add_request(request)
            batch.add_request(changeset)

        if "update" is oRequests and oRequests.update:
            changeset = self._service_instance.create_changeset()
            for oReq in oRequests.update:
                request = self.prepareUpdateRequest(oReq)
                if not request is None:
                    changeset.add_request(request)
            batch.add_request(changeset)

        response = batch.execute()
        print(response)

    def prepareReadRequest(self, oRequest):
        if not oRequest["entityName"]:
            return
        if not oRequest["entityKey"]:
            return

        read_request = self.getEntitySet(
            oRequest["entityName"]).get_entity(oRequest["entityKey"])

        sSelect = oRequest.get("select", "")
        sExpand = oRequest.get("expand", "")
        if sSelect:
            read_request.select(sSelect)
        if sExpand:
            read_request.expand(sExpand)
        return read_request

    def prepareDeleteRequest(self):
        pass

    def prepareCreateRequest(self, oRequest):
        if not oRequest["entityName"]:
            return
        if not oRequest["data"]:
            return

        create_request = self.getEntitySet(
            oRequest["entityName"]).create_entity()
        create_request.set(**oRequest["data"])
        return create_request

    def prepareUpdateRequest(slef):
        pass

    def fetchCSRFToken(self):
        sToken = self._session.headers.get("x-csrf-token", "")
        if not sToken:
            oResponse = self._session.head(self._service_url, headers={
                                           'x-csrf-token': 'fetch'})
            sToken = oResponse.headers.get('x-csrf-token', '')
            self._session.headers.update( {'x-csrf-token': sToken })
            # self._service_instance.http_get()
