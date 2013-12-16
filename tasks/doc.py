# -*- coding: utf-8 -*-
from invoke import task, run, Collection

@task(default=True)
def make(builder='html'):
    run('make -C docs/ %s' % builder)

@task
def clean():
    run('git clean -Xdf')
    run('rm -rf docs/_build')

ns = Collection(make, clean)
