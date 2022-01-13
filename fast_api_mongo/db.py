from pymongo import MongoClient


conn = MongoClient("mongodb+srv://shayaomer:Omer987654@cluster0.oq1lh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
comp_db = conn["windows_scanner_db"]
collection = comp_db["id_sftw_cve"]

