from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from app.config import Config
import pymysql
from flask_swagger_ui import get_swaggerui_blueprint


pymysql.install_as_MySQLdb()

app = Flask(__name__)
db = SQLAlchemy(app)

SWAGGER_URL = '/api/docs'
API_URL = 'http://localhost:5000/swagger.json'

if __name__ == '__main__':
    app.config.from_object(Config())
    db = SQLAlchemy(app)
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "World Landmarks"
        },
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )
    app.register_blueprint(swaggerui_blueprint)

    app.run(debug=True, host='0.0.0.0')




