import os
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import json

app = Flask(__name__)

db = SQLAlchemy(app)

app_settings = os.getenv("APP_SETTINGS", "app.config.DevelopmentConfig")
app.config.from_object(app_settings)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"