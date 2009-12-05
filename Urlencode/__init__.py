#!/usr/bin/env python
from __future__ import with_statement

import os

from eventlet import api
from eventlet import greenio
from eventlet import wsgi
from pprint import pprint

from Urlencode import views

static_types = { 
        'png' : 'image/png',
        'jpg' : 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif' : 'image/git',
        'css' : 'text/css',
        'js'  : 'text/javascript',
}

class ReadFile(greenio.GreenFile):
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.close()
        if tb:
            return False
        return True

def app(environ, start_response):
    pprint(environ)
    path = environ['PATH_INFO']
    view = None

    if path == '/':
        view = 'index'
    else:
        path = path[1:]
        view = views.get(path)

    if not view:
        ##
        ## If we don't have a static file, or somebody is giving me a crap URL
        ## I'm just going to bounce them back
        if '..' in path or not path.startswith('static') \
                or not os.path.exists(path):
            start_response('404 Not Found', [('Content-Type', 'text/plain')])
            return ['Not Found\r\n']

        segments = path.split('.')
        if static_types.get(segments[-1]):
            start_response('200 OK', [('Content-Type', static_types[segments[-1]])])
        else:
            start_response('200 OK', [('Content-Type', 'text/plain')])
        fd = None
        try:
            fd = open(path, 'r')
            return fd.read()
        finally:
            if fd:
                fd.close()


    start_response('200 OK', [('Content-Type', 'text/html')])
    output = unicode(views.get(view)(searchList=[environ]))
    return output


