# coding: utf-8
from flask import Blueprint, send_file, send_from_directory
from flask import current_app

angular = Blueprint('angular', __name__)


@angular.route('/')
def index():
    return send_file('templates/index.html')


@angular.route('/partials/<path:filename>')
def partials(filename):
    return send_from_directory(current_app.root_path + '/templates/partials/', filename)