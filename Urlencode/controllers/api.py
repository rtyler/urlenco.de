#!/usr/bin/env python

from Urlencode import controllers

class api(controllers.BaseController):
    content_type = 'text/html'

    @controllers.action(paths=('/Post.aspx',))
    def encode(self, unencoded_url=None, redirect_type='http', **kwargs):
        return self.render('encoded', encoded='http://urlenco.de/fail')

    @controllers.action(paths=('/PostJSON.aspx', '/api/encode'))
    def encode_json(self, **kwargs):
        return '/api/encode'

