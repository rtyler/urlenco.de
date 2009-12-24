#!/usr/bin/env python

from MicroMVC import controller

class api(controller.BaseController):
    content_type = 'text/html'

    @controller.action(paths=('/Post.aspx',))
    def encode(self, unencoded_url=None, redirect_type='http', **kwargs):
        return self.render('encoded', encoded='http://urlenco.de/fail')

    @controller.action(paths=('/PostJSON.aspx', '/api/encode'))
    def encode_json(self, **kwargs):
        return '/api/encode'

    @controller.action(paths=('/Dispatch.aspx',))
    def dispatch(self, encoded_url=None, **kwargs):
        self.code = 301
        self.headers.append( ('Location', encoded_url) )
        return encoded_url
