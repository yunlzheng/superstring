# coding: utf-8
# Test Unit


class TestVolumeResources(object):

    def test_resources_volume_get(self, app):
        assert app.get('/v1/volumes/1').data

    def test_resources_volume_delete(self, app):
        assert app.delete('/v1/volumes/1').data

    def test_resources_volume_put(self, app):
        assert app.put('/v1/volumes/1').data

    def test_resources_volumes_get(self, app):
        assert app.delete('/v1/volumes').data

    def test_resources_volumes_post(self, app):
        assert app.post('/v1/volumes').data