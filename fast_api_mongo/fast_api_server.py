from fastapi import FastAPI
from pydantic import BaseModel
from db import comp_db, collection
import json
import socket

app = FastAPI()

class Comp(BaseModel):
    comp_name: str
    data: json

@app.get('/')
def home():
    return 'Hello, you can upload your scan at endpoint /upload_data ' \
           'and you can ask for a previous scan using a computer name at /get_data'

@app.get('/upload_data')
def upload_data(upload_data):
    return {}

@app.get('/get_data/{comp_id}')
def get_data(comp_id: str):
    return collection.find_one({'_id': comp_id})


