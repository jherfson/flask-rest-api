import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASK_SLOW_DB_QUERY_TIME = 0.2
    JSON_AS_ASCII = False


class DevelopmentConfig(Config):
    params_conn = os.path.join(basedir, 'people.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + params_conn
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True
