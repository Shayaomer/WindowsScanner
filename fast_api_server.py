from fastapi import FastAPI
from pydantic import BaseModel
from db import collection
from main import execute
import socket
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


class Comp(BaseModel):
    comp_name: str
    data: dict or str

    def __init__(self):
        comp_name = str(socket.gethostname())
        self.comp_name = comp_name


@app.get('/')
def home():
    return 'Hello, you can upload your scan at endpoint /upload_data ' \
           'and you can ask for a previous scan using a computer name at /get_data'


@app.get('/get_data/{comp_name}')
def get_data(comp_name: str):
    data = json.dumps(collection.find_one({'_id': comp_name}))
    parsed = json.loads(data)
    parsed['_data'] = json.loads(parsed['_data'])
    return parsed


@app.get('/scan_and_upload')
def scan_and_upload():
    c = Comp()
    c.data = execute()
    collection.insert_one({c})

