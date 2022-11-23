import psycopg2
import datetime
from typing import List, Tuple, Any

class Transaction:
    __tablename__ = "transaction"

    @classmethod
    def get_table_info(cls):
        return { "tablecategory": "Transaction", "tablename": "Transaction" }
    
    @classmethod
    def get_table_details(cls):
        return {**Transaction.get_table_info(), "title": "Transaction Table" }

    @classmethod
    def get_table_fields_info(cls) -> List[Any]:
        return [
            {**Transaction.get_table_info(), "fieldname": "TxnType", "label": "Transaction type", "datatype": "char", "length": "25" },
            {**Transaction.get_table_info(), "fieldname": "TxnID", "iskey": True, "label": "Transaction Id", "datatype": "char", "length": "36" },
            {**Transaction.get_table_info(), "fieldname": "TxnLineID", "label": "Transaction line id", "datatype": "Char", "length": "36" },
            {**Transaction.get_table_info(), "fieldname": "TimeCreated", "label": "Created time", "datatype": "dateTime", "length": "27" },
            {**Transaction.get_table_info(), "fieldname": "TimeModified", "label": "Last changed time", "datatype": "datetime", "length": "27" },
            {**Transaction.get_table_info(), "fieldname": "EntityRefListID", "label": "Entity ref List Id", "datatype": "char", "length": "36" },
            {**Transaction.get_table_info(), "fieldname": "EntityRefFullName", "label": "Entity reference Full Name", "datatype": "char", "length": "209" },
            {**Transaction.get_table_info(), "fieldname": "AccountRefListID", "label": "Account reference Id", "datatype": "char", "length": "36" },
            {**Transaction.get_table_info(), "fieldname": "AccountRefFullName", "label": "Account ref Full Name", "datatype": "char", "length": "159" },
            {**Transaction.get_table_info(), "fieldname": "TxnDate", "label": "Transaction date", "datatype": "date", "length": "10" },
            {**Transaction.get_table_info(), "fieldname": "TxnDateMacro", "label": "Transaction date macro", "datatype": "char", "length": "23" },
            {**Transaction.get_table_info(), "fieldname": "RefNumber", "label": "Reference Numebr", "datatype": "char", "length": "10" },
            {**Transaction.get_table_info(), "fieldname": "Amount", "label": "Amount", "datatype": "char", "length": "11", "decimal": "2" },
            {**Transaction.get_table_info(), "fieldname": "Memo", "label": "Memo", "datatype": "char", "length": "4095" },
            {**Transaction.get_table_info(), "fieldname": "TransactionDetailLevelFilter", "label": "Transaction detail Lvl Filter", "datatype": "char", "length": "23" },
            {**Transaction.get_table_info(), "fieldname": "TransactionPostingStatusFilter", "label": "Transaction posting status filter", "datatype": "char", "length": "23" },
            {**Transaction.get_table_info(), "fieldname": "TransactionPaidStatusFilter", "label": "Transaction paid status filter", "datatype": "char", "length": "23" },
            {**Transaction.get_table_info(), "fieldname": "FQPrimaryKey", "label": "FQ Primary Key", "datatype": "Char", "length": "184" }
        ]

    @classmethod
    def get_fieldnames(cls) -> Tuple:
        afields = []
        for fld in cls.get_table_fields_info():
            afields.append(fld["fieldname"])
        return afields


start_time = datetime.datetime.now()
con = psycopg2.connect(database="auditapp", user="postgres", password="postgres", host="10.192.250.55", port="5432")
print("Database opened successfully")
end_time = datetime.datetime.now()
print(f"connect time { end_time - start_time }")

start_time = datetime.datetime.now()
cur = con.cursor()
cur.execute("SELECT * from transaction")
rows = cur.fetchall()

end_time = datetime.datetime.now()
print(f"select time { end_time - start_time }")


start_time = datetime.datetime.now()
fields = Transaction.get_fieldnames()
aData = []
for row in rows:
    data = {}
    for index, fld in enumerate(fields):
       data[fld] = row[index]
    aData.append(data)

end_time = datetime.datetime.now()
print(f"mapping time { end_time - start_time }")
