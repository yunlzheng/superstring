# coding: utf-8


class DefaultConfig(object):
    DEBUG = True
    SECRET_KEY = 'superstring-secret'

    CACHE_TYPE = 'simple'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dashbord.db'

    SECURITY_LOGIN_URL = '/login'
    SECURITY_LOGOUT_URL = '/logout'

    SECURITY_REGISTERABLE = True
    SECURITY_CHANGEABLE = True

    #i18n
    BABEL_DEFAULT_LOCALE = 'en'