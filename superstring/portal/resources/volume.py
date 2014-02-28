# coding: utf-8
from flask.ext.restful import reqparse
from flask.ext.restful import Resource
from flask.ext.login import login_required
from flask.ext.babel import gettext as _
from superstring.common.extensions import api
from superstring.portal import signals


class VolumesAPI(Resource):
    decorators = [login_required]

    def get(self):
        return [{
                    "status": "available",
                    "usage": 0,
                    "display_name": None,
                    "attachments": [],
                    "availability_zone": "nova",
                    "bootable": "false",
                    "created_at": "2014-02-18T05:24:33.281325",
                    "pool_id": 1,
                    "display_description": None,
                    "os-vol-host-attr:host": "cc.huacloud.demo",
                    "volume_type": "None",
                    "snapshot_id": None,
                    "source_volid": None,
                    "os-vol-mig-status-attr:name_id": None,
                    "metadata": {
                        "null": None
                    },
                    "id": "27d6ccc6-f278-45fc-bde7-7a4d07ecd29f",
                    "os-vol-mig-status-attr:migstat": None,
                    "size": 1
                }]

    def post(self):
        signals.volume_create_start.send()
        # TODO: 逻辑代码
        signals.volume_create_end.send()


class VolumeAPI(Resource):
    #decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True, help=_('No task title provided'), location='json')
        self.reqparse.add_argument('description', type=str, default="", location='json')
        super(VolumeAPI, self).__init__()

    def get(self, id):
        return {
            "status": "available",
            "usage": 0,
            "display_name": None,
            "attachments": [],
            "availability_zone": "nova",
            "bootable": "false",
            "created_at": "2014-02-18T05:24:33.281325",
            "pool_id": 1,
            "display_description": None,
            "os-vol-host-attr:host": "cc.huacloud.demo",
            "volume_type": "None",
            "snapshot_id": None,
            "source_volid": None,
            "os-vol-mig-status-attr:name_id": None,
            "metadata": {
                "null": None
            },
            "id": id,
            "os-vol-mig-status-attr:migstat": None,
            "size": 1
        }

    def put(self, id):
        args = self.reqparse.parse_args()

    def delete(self, id):
        pass


api.add_resource(VolumesAPI, '/api/volumes', endpoint='tasks')
api.add_resource(VolumeAPI, '/api/volumes/<int:id>', endpoint='task')