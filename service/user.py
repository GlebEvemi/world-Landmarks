from bcrypt import hashpw, checkpw
from models.User import User
from datetime import datetime
from app import db

def str_to_bytes(s: str) -> bytes:
    return bytes([ord(char) for char in s])


def create_user(username: str, email: str, password: str) -> User:
    bpwd = str_to_bytes(password) 
    bsalt = str_to_bytes(username+email)
    usr = User(username, email, hashpw(bpwd, bsalt).decode(), datetime.now())

    return usr
