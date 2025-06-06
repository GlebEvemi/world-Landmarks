from functools import wraps
from flask import request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from models.User import User

def authorized(f):
    def fn(*args, **kwargs):
        try:
            verify_jwt_in_request()
            identity = get_jwt_identity()

            user = User.query.filter_by(id = identity).first()

            if not user:
                raise ValueError("User not found")

            return f(user)
        except Exception as e: 
            print(e)
            return {
                "error": "Forbidden"
            }, 403
    return fn
