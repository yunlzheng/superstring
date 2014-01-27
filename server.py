from gevent import monkey; monkey.patch_socket(); monkey.patch_thread();
from gevent.pywsgi import WSGIServer

from superstring.portal.application import create_app


if __name__ == '__main__':
    print('Serving on 5000 ...')
    app = create_app()
    WSGIServer(('', 5000), app).serve_forever()