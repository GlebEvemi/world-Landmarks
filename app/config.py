from os import environ
from dotenv import load_dotenv

load_dotenv()
print("Loading config...")
class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = "VeryVerySecretKey"
    SQLALCHEMY_DATABASE_URI = f"mysql://{environ['DB_USER']}:{environ['DB_PASSWORD']}@{environ['DB_HOST']}/{environ['DATABASE']}"
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
