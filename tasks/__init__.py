# -*- coding: utf-8 -*-
from invoke import Collection

from .doc import ns as doc_ns
from .test import ns as test_ns

ns = Collection(
    doc=doc_ns,
    test=test_ns,
)
