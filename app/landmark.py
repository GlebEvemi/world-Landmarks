from app import app
from app.middlewares.authorize import authorized
from models import User
from service.user import create_user, login_user
from datetime import timedelta
from flask import jsonify
from service.user import create_user
from flask import request
from flask_jwt_extended import create_access_token
from datetime import timedelta

@app.route("/landmark", methods=["POST"])
@authorized
def create_landmark(user: User.User):
    return "Unimplemented", 501


@app.route("/landmark", methods=["POST"])
@authorized
def update_landmark(user: User.User):
    return "Unimplemented", 501


@app.route("/landmark", methods=["POST"])
@authorized
def delete_landmark(user: User.User):
    return "Unimplemented", 501

