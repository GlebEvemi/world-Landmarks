from bcrypt import hashpw, checkpw, gensalt
from models.User import User
from datetime import datetime
from app import db, user
from sqlalchemy import or_

def str_to_bytes(s: str) -> bytes:
    return bytes([ord(char) for char in s])


def create_user(username: str, email: str, password: str) -> User:
    existing = User.query.filter_by(username=username).first()
    if existing:
        raise ValueError("User with this username already exists.")

    existing = User.query.filter_by(email=email).first()
    if existing:
        raise ValueError("User with this email already exists.")
    bpwd = str_to_bytes(password) 
    bsalt = gensalt()
    usr = User(username, email, hashpw(bpwd, bsalt).decode(), datetime.now())
    db.session.add(usr)
    db.session.commit()
    return usr


def login_user(username_or_email: str, password: str) -> User:
    first = User.query.filter(
        or_(
            User.username == username_or_email,
            User.email == username_or_email,
        )
    ).first()
    if not first:
        raise ValueError("Wrong credentials")
    if not checkpw(str_to_bytes(password), str_to_bytes(first.password)):
        raise ValueError("Wrong credentials")

    return first
