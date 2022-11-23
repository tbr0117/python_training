from pydantic import BaseModel

class Person(BaseModel):
    id: int
    name: str

per1 = Person(
    id= 232,
    name="Str",
)
print(per1.schema())
print(per1.schema_json())

assert per1.id == 231