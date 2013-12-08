# -*- coding: utf-8 -*-
import pytest

@pytest.yield_fixture
def passwd():
    print('setup befor yield')
    f = open('/etc/passwd')
    yield f.readlines()
    print('teardown after yield')

def test_has_lines(passwd):
    print('test called')
    assert passwd
