# FastAPI

## Table of Contents

- [FastAPI](#fastapi)
  - [Table of Contents](#table-of-contents)
  - [Sources](#sources)
  - [Basics](#basics)

## Sources

- []()

## Basics

- FastAPI is a tool for building web applications in Python.

- To start a server with a running FastAPI: ```uvicorn [file_name]:[app_name] --reload```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world again"}

@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}

# It is possible to send JSON to FastAPI
from pydantic import BaseModel, validator

# To define required JSON type use BaseModel class from pydantic
class Item(BaseModel):
    name: str
    price: float

    # JSON can have multiple different types and to confirm that
    # received format is correct we can use validator that is part of pydantic
    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"we expect price >= 0, we received {value}")
        return value

@app.post("/items/")
def create_item(item: Item):
    """
    Example of a docstring.
    """
    return item

# async code in FastAPI
import time
import asyncio

@app.get("/sleep_slow")
def sleep_slow():
    time.sleep(1)
    return {"status": "done"}

@app.get("/sleep_fast")
async def sleep_fast():
    await asyncio.sleep(1)
    return {"status": "done"}


```

- Documentation is available in */docs* where Swagger UI lists all of the methods. Additional descriptions are taken from the docstring.

- Web APIs can be tested using ```boom```. In both commands ```boom``` will send a total of (defined via ```-n```) 200 requests and will do it with a concurrency of 200 (defined via ```-c```):

```python
boom http://127.0.0.1:8000/sleep_slow -c 200 -n 200
boom http://127.0.0.1:8000/sleep_fast -c 200 -n 200
```

- Testing FastAPI:

```python
from starlette.testclient import TestClient
from app import app

client = TestClient(app)

def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "hello world again"}

def test_users_endpoint():
    resp = client.get("/users/1")
    assert resp.status_code == 200
    assert resp.json() == {"user_id": "1"}

def test_correct_item():
    json_blob = {"name": "shampoo", "price": 1.5}
    resp = client.post("/items/", json=json_blob)
    assert resp.status_code == 200

def test_wrong_item():
    json_blob = {"name": "shampoo", "price": -1.5}
    resp = client.post("/items/", json=json_blob)
    assert resp.status_code != 200
```