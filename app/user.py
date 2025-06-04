from app import app
from service.user import create_user
from datetime import timedelta
from flask import jsonify
from service.user import create_user
from flask import request
from flask_jwt_extended import create_access_token
from datetime import timedelta


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
                user.id, 
                expires_delta=timedelta(minutes=3)
            )

            return jsonify(user_dict), 200
    except ValueError as e:
        return jsonify({
            "error": e.__str__()
        }), 400
