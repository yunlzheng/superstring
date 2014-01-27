# -*- coding: utf-8 -*-
from flask import Flask

from superstring.portal.frontend import *
from superstring.common.extensions import db

DEFAULT_APP_NAME = __name__

__all__ = ['create_app']

DEFAULT_BLUEPRINTS = [
    (frontend, '')
]


def create_app(config=None, app_name=None, blueprints=None):
    """
    Create flask application instance
    @param config: config object
    @param app_name: flask application name
    @param blueprints: flask blueprints
    @return: app
    """
    if app_name is None:
        app_name = DEFAULT_APP_NAME
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name)
    configure_app(app, config)
    configure_extensions(app)
    configure_blueprint(app, blueprints)
    return app


def configure_app(application, config):
    """
    Configure application from object and envvar
    @param application: flask application instance
    @param config: config object
    """
    if config:
        application.config.from_object(config)
    application.config.from_envvar('SUPERSTRING_PORTAL_SETTINGS', silent=True)


def configure_blueprint(application, blueprints):
    """
    Configure flask blueprint
    @param application: flask application instance
    @param blueprints: flask blueprint tuple
    """
    for blueprint, url_prefix in blueprints:
        application.register_blueprint(blueprint, url_prefix=url_prefix)


def configure_extensions(application):
    """
    Configure flask applicat ext
    @param application:
    """
    db.init_app(application)
    #cache.init_app(application)


if __name__ == '__main__':
    app = create_app().run(debug=True)
