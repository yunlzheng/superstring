# -*- coding: utf-8 -*-
from gevent import monkey; monkey.patch_socket();
from gevent.pywsgi import WSGIServer

from application import create_app


if __name__ == '__main__':
    print('Serving on 5000 ...')
    app = create_app()
    app.debug = True
    app.run(5000)
    #WSGIServer(('', 5000), create_app()).serve_forever()
