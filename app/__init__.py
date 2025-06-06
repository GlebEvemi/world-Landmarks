from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import pymysql
from flask_jwt_extended import JWTManager
from flasgger import Swagger


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config())
db: SQLAlchemy = SQLAlchemy(app)
jwt = JWTManager(app)
swagger = Swagger(app, template_file="apispec.yaml")
