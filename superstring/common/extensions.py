# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache

__all__ = ['db', 'cache']

db = SQLAlchemy()
cache = Cache()
