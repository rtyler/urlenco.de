#!/usr/bin/env python

from Urlencode import controllers

class home(controllers.BaseController):
    content_type = 'text/html'

    @controllers.action(paths=('/', '/Default.aspx'))
    def index(self, **kwargs):
        return self.render('index')

    @controllers.action()
    def about(self, **kwargs):
        return self.render('about')

    @controllers.action(paths=('/Developer.aspx',))
    def developers(self, **kwargs):
        return 'Developers'

    @controllers.action(paths=('/Stats.aspx',))
    def stats(self, **kwargs):
        return 'Stats'
