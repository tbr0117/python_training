from lib2to3.pgen2.token import OP
from typing import List, Optional, Any
from pydantic import BaseModel

user_dict = {
        "name": "RAM",
        "age": 32,
        "phno": 4324,
        "isDeveloper": True
    }

# user_dict

class UserTemplate(BaseModel): # schemas
    name: str
    age: int
    phno: Optional[int]
    isDeveloper: bool = True
    info: Any


user_temp = UserTemplate(name="RAm", age=43,phno=564,isDeveloper=False)



def myInfo(name:str):
    return name

def updateUser(name:str, age:int, phno:int, isDeveloper:bool)-> UserTemplate:
    return UserTemplate(**{
        "name": name,
        "age": age,
        "phno": phno,
        "isDeveloper": isDeveloper
    })

def updateUserWithTempalate(user:UserTemplate):
    print(user.name, user.isDeveloper)


updateUserWithTempalate()   

updateUser(name="23423", age=32, phno=32, isDeveloper=True)

def users(names:Optional[List[str]], count:Optional[int] = 0):
    pass

users()