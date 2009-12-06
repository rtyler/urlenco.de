#!/usr/bin/env python
from __future__ import with_statement

import os

from eventlet import api
from eventlet import greenio
from eventlet import wsgi
from pprint import pprint

from Urlencode import controllers
from Urlencode import views

static_types = { 
        'png' : 'image/png',
        'jpg' : 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif' : 'image/git',
        'css' : 'text/css',
        'js'  : 'text/javascript',
}

def app(environ, start_response):
    pprint(environ)
    path = environ['PATH_INFO']
    controller = controllers.get(path)

    if controller:
        klass, attr = controller
        controller = klass(start_response, **environ)
        controller.prepare()
        return [getattr(klass, attr)(controller) + '\r\n']

    ##
    ## If we don't have a static file, or somebody is giving me a crap URL
    ## I'm just going to bounce them back
    if '..' in path or not path.startswith('/static') \
            or not os.path.exists(os.getcwd() + path):
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ['Not Found\r\n']

    segments = path.split('.')
    if static_types.get(segments[-1]):
        start_response('200 OK', [('Content-Type', static_types[segments[-1]])])
    else:
        start_response('200 OK', [('Content-Type', 'text/plain')])
    fd = None
    try:
        fd = open(os.getcwd() + path, 'r')
        return [fd.read()]
    finally:
        if fd:
            fd.close()

