# coding: utf-8
from flask import Blueprint, send_file, send_from_directory

print '/%s' % __name__
frontend = Blueprint('frontend', __name__, static_folder='static', static_url_path='/statics')


@frontend.route('/')
def index():
    return send_file(frontend.root_path+'/templates/index.html')


@frontend.route('/partials/<path:filename>')
def partials(filename):
    return send_from_directory(frontend.root_path + '/templates/partials/', filename)