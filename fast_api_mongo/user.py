from pydantic import BaseModel

class User(BaseMode):
    comp_id: str
    prog_cve: (str, list)