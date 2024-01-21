import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']

DATABASE_URL = f"mysql+pymysql://root:{MYSQL_ROOT_PASSWORD}@db/{MYSQL_DATABASE}"


class BaseConfig:
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
}
