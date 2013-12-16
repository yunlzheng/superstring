# # -*- coding: utf-8 -*-
import pytest

from superstring.application import app as real_app

@pytest.fixture(scope='session')
def app(request):
    return real_app.test_client()
