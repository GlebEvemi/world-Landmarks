from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import pymysql
from flask import jsonify

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)


@app.route("/user/register")
def register():
    data = {"message": "Hello, World!"}

    return jsonify(data), 200
