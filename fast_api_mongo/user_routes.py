from fastapi import APIRouter

from user import User
from db import conn

user = APIRouter()

@user.get('/')
async def find_all_user():
    return conn.local.user.find()

