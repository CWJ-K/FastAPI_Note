from enum import Enum
from fastapi import FastAPI, Path


class UserType(str, Enum):
    STANDARD = 'standard'
    ADMIN = 'admin'

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'hello': 'world'}


@app.get('/users/{id}')
async def get_user(id: int):
    return {'id': id}


@app.get('/users/{type}/{id}/')
async def get_user(type: str, id: int):
    return {'type': type,'id': id}


@app.get('/user/{type}/{id}/')
async def get_user(type: UserType, id: int):
    return {'type': type, 'id': id}


@app.get('/users/{id}')
async def get_user(id: int = Path(..., ge=1)):
    return {'id': id} 