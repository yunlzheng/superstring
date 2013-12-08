# -*- coding: utf-8 -*-
import pytest
from invoke import task, Collection

@task(default=True)
def all():
    """
    全部测试
    """
    pytest.main('tests')

ns = Collection(all)
