# # -*- coding: utf-8 -*-
# import pytest

# @pytest.fixture(scope='module', params=['testa', 'testb'])
# def smtp(request):
#     def fin():
#         print('teardown smtp')
#     request.addfinalizer(fin)
#     print('*' * 20, request.param)
#     return 1


# class App(object):

#     def __init__(self, smtp):
#         self.smtp = smtp

# @pytest.fixture(scope='module')
# def app(smtp):
#     return App(smtp)

