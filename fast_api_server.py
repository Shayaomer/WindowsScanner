from fastapi import FastAPI
from db import collection
from main import execute
import socket
import json


app = FastAPI()


@app.get('/')
def home():
    return 'Hello, you can scan and upload at endpoint /scan_and_upload' \
           'and you can ask for a previous scan using a computer name at /get_data/{computer_name}'


@app.get('/get_data/{comp_name}')
def get_data(comp_name: str):
    data = collection.find_one({'_id': comp_name})
    parsed = json.loads(data['_data'])
    return parsed


@app.get('/scan_and_upload')
def scan_and_upload():
    c = execute()
    comp_name = str(socket.gethostname())
    if collection.find_one({'_id': comp_name}) == None:
        collection.insert_one(c)
    else:
        collection.delete_one({'_id': comp_name})
        collection.insert_one(c)
    return {'val': 'Scan has been uploaded to the database.'}

