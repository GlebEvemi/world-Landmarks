from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import pymysql
from flask import jsonify
from service.user import create_user
from flask import request

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)


@app.route("/user/register", methods=["POST"])
def register():
    data = request.get_json()
    with app.app_context():
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        user = create_user(username, email, password)

        return jsonify(user), 200
