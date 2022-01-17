from pymongo import MongoClient

conn = MongoClient("mongodb+srv://shayaomer:Omer987654@cluster0.oq1lh.mongodb.net/scanner_db?retryWrites=true&w=majority")
db = conn["scanner_db"]
collection = db["id_sftw_cve"]
