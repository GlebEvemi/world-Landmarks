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


EXPIRES_DELTA = timedelta(hours=3)


@app.route("/user/register", methods=["POST"])
def register():
    data = request.get_json()
    try:
        with app.app_context():
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            user = create_user(username, email, password)
            user_dict = user.to_dict()
            user_dict["access_token"] = create_access_token(
                str(user.id), 
                expires_delta=EXPIRES_DELTA
            )

            return jsonify(user_dict), 200
    except ValueError as e:
        return jsonify({
            "error": e.__str__()
        }), 400


@app.route("/user/login", methods=["POST"])
def login():
    data = request.get_json()

    try:
        with app.app_context():
            login = data.get("login")
            password = data.get("password")
            user = login_user(login, password)
            user_dict = user.to_dict()
            user_dict["access_token"] = create_access_token(
                str(user.id),
                expires_delta=EXPIRES_DELTA
            )
            return user_dict, 200
    except ValueError as e:
        return jsonify({
            "error": e.__str__()
        }), 400


@app.route("/user/me")
@authorized
def current_user(user: User.User):
    return user.to_dict(), 200
