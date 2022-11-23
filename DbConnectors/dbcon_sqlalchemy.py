from sqlalchemy import String, Float, Column, DateTime,Date
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Tuple, Any
Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transaction"
    TxnID	= Column(String,primary_key=True, nullable=False)
    TxnLineID = Column(String, nullable=False)
    TxnType = Column(String, nullable=False)
    TimeCreated = Column(DateTime)
    TimeModified = Column(DateTime) 
    EntityRefListID= Column(String)
    EntityRefFullName= Column(String)
    AccountRefListID= Column(String)
    AccountRefFullName= Column(String)
    TxnDate = Column(Date)
    TxnDateMacro = Column(String)
    RefNumber = Column(String)
    Amount= Column(Float,nullable=False)
    Memo = Column(String)
    TransactionDetailLevelFilter = Column(String)
    TransactionPostingStatusFilter = Column(String)
    TransactionPaidStatusFilter= Column(String)
    FQPrimaryKey = Column(String)

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

    def get_fieldnames(cls) -> Tuple:
            afields = tuple()
            for fld in cls.get_table_fields_info():
                afields.append(fld["fieldname"])


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import PostgresDsn
import datetime

start_time = datetime.datetime.now()
SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
            scheme="postgresql",
            user="postgres",
            password="postgres",
            host="10.192.250.55:5432",
            path=f"/auditapp",
            query="options=-csearch_path=information_schema"
        )

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True) # , connect_args={'options': '-csearch_path=information_schema'}

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()

# db: Session = SessionLocal()
# end_time = datetime.datetime.now()

# print(f"connection time { end_time - start_time }")

# start_time = datetime.datetime.now()

# aData = db.query(Transaction).all()

# end_time = datetime.datetime.now()
# print(f"Select Time { end_time - start_time }")



start_time = datetime.datetime.now()
with engine.connect() as conn:
    end_time = datetime.datetime.now()
    print(f"Engine Time { end_time - start_time }")

    start_time = datetime.datetime.now()
    # rows = conn.execute("SELECT * from transaction")
    cols = conn.execute("SELECT * from columns")
    
    # print(f"rows { len(rows)}")
    end_time = datetime.datetime.now()
    print(f"Engine Time { end_time - start_time }")
