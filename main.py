from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"