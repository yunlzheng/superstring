# coding: utf-8
# Flask Resource API Template
from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from flask.ext.login import login_required

from superstring.common.extensions import api
from superstring.portal import signals


class VmAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(VmAPI, self).__init__()

    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class VmsAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(VmsAPI, self).__init__()

    def get(self):
        pass

    def post(self):
        signals.vm_create_start.send()
        # TODO: 逻辑代码
        signals.vm_create_end.send()

api.add_resource(VmsAPI, '/api/vms', endpoint='vms')
api.add_resource(VmAPI, '/api/vm/<int:id>', endpoint='vm')