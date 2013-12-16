# -*- coding: utf-8 -*-
from gevent.pywsgi import WSGIServer

from application import app


if __name__ == '__main__':
    print('Serving on 5000 ...')
    WSGIServer(('', 5000), app).serve_forever()
