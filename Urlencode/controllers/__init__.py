#!/usr/bin/env python
from __future__ import with_statement

import os
import sys

def __mapControllers():
    cont_dir = os.path.dirname(__file__)

    for controller in os.listdir(cont_dir):
        if not controller.endswith('.py'):
            continue
        if controller == '__init__.py':
            continue

        name = controller.replace('.py', '')
        print name
        __import__('Urlencode.controllers.%s' % name)
        module = sys.modules.get('Urlencode.controllers.%s' % name)
        klass = getattr(module, name, None)

        if not klass:
            continue

        for p in module.paths:
            yield (p, klass)

controllers = None

def get(name, default=None):
    global controllers
    if not controllers:
        controllers = dict(__mapControllers())
    return controllers.get(name, default)


class GenericControllerException(Exception):
    pass

code_map = {
        200 : '200 OK',
        404 : '404 Not Found',
}

class BaseController(object):
    content_type = 'text/plain'
    _start = None
    code = 200

    def __init__(self, start_response, **kwargs):
        self.__dict__.update(kwargs)
        self._start = start_response

    def prepare(self):
        self._start(code_map[self.code], [('Content-Type', self.content_type)])

    def execute(self, *args, **kwargs):
        raise GenericControllerException('%s must implement an execute method' % self.__class__.__name__)


