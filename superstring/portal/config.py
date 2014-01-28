# coding: utf-8


class DefaultConfig(object):
    DEBUG = True
    SECRET_KEY = 'superstring-secret'

    CACHE_TYPE = 'simple'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dashbord.db'