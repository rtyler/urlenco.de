#!/usr/bin/env python

from MicroMVC import controller
from Urlencode import controllers

class home(controllers.DBController):
    content_type = 'text/html'

    @controller.action(paths=('/', '/Default.aspx'))
    def index(self, **kwargs):
        return self.render('index')

    @controller.action()
    def about(self, **kwargs):
        return self.render('about')

    @controller.action(paths=('/developers', '/Developer.aspx',))
    def developers(self, **kwargs):
        return self.render('developers')

    @controller.action(paths=('/stats', '/Stats.aspx',))
    def stats(self, **kwargs):
        return self.render('stats')
