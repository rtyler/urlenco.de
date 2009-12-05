#!/usr/bin/env python

import sys
from eventlet import api
from eventlet import wsgi

import Urlencode

def main():
    wsgi.server(api.tcp_listener(('', 8080)), Urlencode.app)
    return 0

if __name__ == '__main__':
    sys.exit(main())

