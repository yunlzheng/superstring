# # -*- coding: utf-8 -*-
import pytest
#
from superstring.portal.application import create_app


@pytest.fixture(scope='session')
def app(request):
    return create_app().test_client()