#!/usr/bin/env python

from Urlencode import controllers
from Urlencode import views

class home(controllers.BaseController):
    content_type = 'text/html'

    @controllers.action(paths=('/', '/Default.aspx'))
    def index(self, **kwargs):
        return self.render('index')

    @controllers.action()
    def about(self, **kwargs):
        return self.render('about')


