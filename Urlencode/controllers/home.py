#!/usr/bin/env python

from Urlencode import controllers
from Urlencode import views

paths = ('/', '/index.html', '/index', '/Default.aspx',)

class index(controllers.BaseController):
    content_type = 'text/html'

    def execute(self, **kwargs):
        return unicode(views.get('index')(searchList=[{'controller' : self}]))


