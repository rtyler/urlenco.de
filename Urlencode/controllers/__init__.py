#!/usr/bin/env python
from __future__ import with_statement

import logging
import os
import sys
import types

from Urlencode import views

def __mapControllers():
    cont_dir = os.path.dirname(__file__)

    for controller in os.listdir(cont_dir):
        if not controller.endswith('.py'):
            continue
        if controller == '__init__.py':
            continue

        name = controller.replace('.py', '')
        __import__('Urlencode.controllers.%s' % name)
        module = sys.modules.get('Urlencode.controllers.%s' % name)
        klass = getattr(module, name, None)

        if not klass:
            continue

        for attr in dir(klass):
            o = getattr(klass, attr)
            if not isinstance(o, (types.FunctionType, types.MethodType)):
                continue

            if not getattr(o, 'paths', False):
                continue

            for path in getattr(o, 'paths'):
                yield (path, (klass, attr))

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

def action(**kwargs):
    def inner_f(method):
        paths = ('/' + method.func_name,)
        if kwargs.get('paths'):
            paths = paths + kwargs['paths']
        method.paths = paths
        return method
    return inner_f

class BaseController(object):
    content_type = 'text/plain'
    _start = None
    code = 200

    def __init__(self, start_response, **kwargs):
        self.__dict__.update(kwargs)
        self._start = start_response

    def prepare(self):
        self._start(code_map[self.code], [('Content-Type', self.content_type)])

    def render(self, name, **kwargs):
        kwargs.update({'controller' : self})
        template = views.get(name)
        if not template:
            raise GenericControllerException('Could not find "%s" view' % name)
        return unicode(template(searchList=[kwargs]))


