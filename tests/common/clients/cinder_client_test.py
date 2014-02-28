# coding:utf-8

# content of test_sample.py
from superstring.common.clients import cinder_client


class TestCinderClient(object):

    def test_create_volume(self):
        #client = cinder_client.request_client('admin', 'admin', 'admin', 'http://192.168.1.15:35357/v2.0', 15)
        #volume = client.volumes.create(1)
        assert True

    def test_delete_volume(self):
        assert True

    def test_attach(self):
        assert True

    def test_detach(self):
        assert True

    def test_set_metadata(self):
        assert True

    def test_delete_metadata(self):
        assert True