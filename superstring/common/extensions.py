# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache
from flask.ext.login import LoginManager

__all__ = ['db', 'cache']

db = SQLAlchemy()
cache = Cache()
login_manager = LoginManager()
