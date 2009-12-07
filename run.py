#!/usr/bin/env python

import sys

from eventlet import api
from eventlet import wsgi
from eventlet import util
util.wrap_socket_with_coroutine_socket()

import Urlencode

def main():
    try:
        wsgi.server(api.tcp_listener(('', 8081)), Urlencode.app)
    except KeyboardInterrupt:
        print '>>> Exiting cleanly...'
        return 0
    finally:
        return -1

if __name__ == '__main__':
    sys.exit(main())

