# -*- coding: utf-8 -*-
from flask import Flask

from superstring.common.database import db

app = Flask(__name__)
app.config.from_envvar('SUPERSTRING_PORTAL_SETTINGS', silent=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>'
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True)
