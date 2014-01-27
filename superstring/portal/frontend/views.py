# coding: utf-8
from flask import Blueprint, send_file, send_from_directory
from flask import current_app

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return send_file('templates/index.html')


@frontend.route('/partials/<path:filename>')
def partials(filename):
    return send_from_directory(current_app.root_path + '/templates/partials/', filename)