from core.ServiceBase import ServiceBase

service_url = 'http://services.odata.org/V2/Northwind/Northwind.svc/'
service_base = ServiceBase(service_url, '510')


def get_entity_set():
    oRequest = {
        "entityName": "Customers",
        "select": "CustomerID, CompanyName, ContactTitle, Country",
        "filter": "Country eq 'Germany'",
        "count": "inline",
        "top": 20
    }
    Customers_response = service_base.readEntitySet(oRequest)
    # Customer = service_base.readEntity()

    for employee in Customers_response:
        if employee:
            print(employee)


def read_entity():
    oRequest = {
        "entityName": "Customers",
        "entityKey": "BLONP",
        "expand": "Orders"
    }
    customer_response = service_base.readEntity(oRequest)
    print(customer_response)


def create_entity():
    oData = {
        'FirstName': 'Mark',
        'LastName': 'Goody',
        'Address': {
            'HouseNumber': 42,
            'Street': 'Paradise',
            'City': 'Heaven'
        }
    }
    oRequest = {
        "entityName": "Employees",
        "data": oData
    }
    emplayee_response = service_base.createEntity(oRequest)
    print(emplayee_response)
    pass


def process_batch():
    aReadRequests = [
        {
            "entityName": "Customers",
            "entityKey": "BLONP",
            "expand": "Orders"
        },
        {
            "entityName": "Employees",
            "entityKey": "1",
        }
    ]

    oRequests = {
        "read": aReadRequests
    }
    customer_response = service_base.processBatch(oRequests)
    print(customer_response)
    pass


# get_entity_set()

read_entity()

# create_entity()

# process_batch()
