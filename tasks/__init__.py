# -*- coding: utf-8 -*-
from invoke import Collection

from .test import ns as test_ns

ns = Collection(test=test_ns)
