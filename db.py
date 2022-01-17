from pymongo import MongoClient
import json

conn = MongoClient("mongodb+srv://shayaomer:Omer987654@cluster0.oq1lh.mongodb.net/scanner_db?retryWrites=true&w=majority")
db = conn["scanner_db"]
collection = db["id_sftw_cve"]

# data = collection.find_one({'_id': 'Omers-COMP'})
# data = json.loads(json.dumps(data))
# print(type(data))
