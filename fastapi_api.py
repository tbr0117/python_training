from typing import Optional

from fastapi import FastAPI

app = FastAPI(openapi_url="v1/openapi.json")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}