# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache
from flask.ext.login import LoginManager
from flask.ext.security import Security
from flask.ext.restful import Api

__all__ = ['db', 'cache']

db = SQLAlchemy()
cache = Cache()
login_manager = LoginManager()
security = Security()
user_datastore = object()
api = Api()

