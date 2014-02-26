# -*- coding: utf-8 -*-
from flask import Flask
from flask import g
from flask.ext.security import SQLAlchemyUserDatastore

from superstring.portal.config import DefaultConfig
from superstring.portal.frontend import *
from superstring.portal.resources import *
from superstring.common.extensions import db
from superstring.common.extensions import cache
from superstring.common.extensions import login_manager
from superstring.common.extensions import security
from superstring.common.extensions import api
from superstring.portal.security.models import User, Role

DEFAULT_APP_NAME = __name__

__all__ = ['create_app']

DEFAULT_BLUEPRINTS = [
    (frontend, '')
]

user_datastore = SQLAlchemyUserDatastore(db, User, Role)


def create_app(config=None, app_name=None, blueprints=None):
    """
    Create flask app instance
    @param config: config object
    @param app_name: flask app name
    @param blueprints: flask blueprints
    @return: app
    """
    if app_name is None:
        app_name = DEFAULT_APP_NAME
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    if config is None:
        config = DefaultConfig
    app = Flask(app_name)
    configure_app(app, config)
    configure_resources_api()
    configure_extensions(app)
    configure_blueprint(app, blueprints)
    configure_before_handlers(app)
    return app


def configure_app(app, config):
    """
    Configure app from object and envvar
    @param app: flask app instance
    @param config: config object
    """
    if config:
        app.config.from_object(config)
    app.config.from_envvar('SUPERSTRING_PORTAL_SETTINGS', silent=True)


def configure_before_handlers(app):
    @app.before_first_request
    def create_user():
        #try:
        #    db.create_all()
        #    user_datastore.create_user(email='admin@123', password='admin123')
        #    db.session.commit()
        #except Exception as ex:
        #    pass
        pass

    @app.before_request
    def authenticate():
        g.user = getattr(g.identity, 'user', None)


def configure_blueprint(app, blueprints):
    """
    Configure flask blueprint
    @param app: flask app instance
    @param blueprints: flask blueprint tuple
    """
    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)


def configure_resources_api():

    api.add_resource(VolumesAPI, '/api/volumes')
    api.add_resource(VolumeAPI, '/volume/api/v1.0/volumes/<int:id>')


def configure_extensions(app):
    """
    Configure flask applicat ext
    @param app:
    """
    db.init_app(app)
    login_manager.init_app(app)
    security.init_app(app, user_datastore)
    cache.init_app(app)

    api.init_app(app)



if __name__ == '__main__':
    app = create_app().run(debug=True)
