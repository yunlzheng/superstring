# -*- coding: utf-8 -*-
from flask import Flask
from flask import send_file, send_from_directory

from superstring.common.database import db

app = Flask(__name__)
app.config.from_envvar('SUPERSTRING_PORTAL_SETTINGS', silent=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>'
db.init_app(app)

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/partials/<path:filename>')
def partials(filename):
    return send_from_directory(app.root_path+'/templates/partials/', filename)

if __name__ == '__main__':
    app.run(debug=True)
