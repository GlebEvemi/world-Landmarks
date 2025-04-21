import os


class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = "VeryVerySecretKey"
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/db_landmarks"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_TOKEN_EXPIRATION_DAYS = 30
    AUTH_TOKEN_EXPIRATION_SECONDS = 0

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        "mysql://root:@localhost/db_landmarks"
    )



app_config = {
    "development": DevelopmentConfig
}