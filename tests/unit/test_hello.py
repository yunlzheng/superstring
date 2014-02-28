# -*- coding: utf-8 -*-
def test_hello(app):
    assert app.get('/').data
