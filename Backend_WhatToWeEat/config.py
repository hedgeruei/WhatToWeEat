"""

    app 設定檔

    create by : jay
    create at : 2022/06/28

"""

import os

class Config:
    """ 基礎設定 """

    SECRET_KEY = os.environ.get("SECRET_KEY") or "test"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConig(Config):
    """ 開發時的設定檔 """

    DB_HOST = os.environ.get("DEV_DB_HOST")
    DB_PORT = os.environ.get("DEV_DB_PORT")
    DB_USER = os.environ.get("DEV_DB_USER")
    DB_PWD = os.environ.get("DEV_DB_PWD")
    DB_NAME = os.environ.get("DEV_DB_NAME")

    SQLALCHEMY_DATABASE_URI = f"\
    postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}\
    "

    DEBUG = True

class TestConfig(Config):
    """ 測試時的設定檔 """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL") or "sqlite://"

class ProductionConfig(Config):
    """ 部署時的設定檔 """

    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_USER = os.environ.get("DB_USER")
    DB_PWD = os.environ.get("DB_PWD")
    DB_NAME = os.environ.get("DB_NAME")

    SQLALCHEMY_DATABASE_URI = f"\
    postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}\
    "

config = {
    "development" : DevelopmentConig,
    "testing" : TestConfig,
    "production" : ProductionConfig,
    "default" : DevelopmentConig
}

