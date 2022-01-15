from fastapi import FastAPI
from pydantic import BaseModel
from db import collection
from main import execute
import socket
import json

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


# Uploads the final_res.json from the folder
@app.get('/upload_data')
def upload_data():
    c = Comp()
    with open('./json_final_res.json', 'r') as f:
        c.data = json.load(f)
        collection.insert_one({c})
    return {'File upload success'}


@app.get('/scan_and_upload')
def scan_and_upload():
    c = Comp()
    c.data = execute()
    collection.insert_one({c})


@app.get('/get_data/{comp_id}')
def get_data(comp_id: str):
    return collection.find_one({'_id': comp_id})
