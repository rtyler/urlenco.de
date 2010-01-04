#!/usr/bin/env python

import MicroMVC

from Urlencode import controllers
from Urlencode import views

class UrlencodeApplication(MicroMVC.Application):
    controller_dir = 'Urlencode.controllers'
    views_dir = 'Urlencode.views'
    def controllers(self):
        return controllers
    def views(self):
        return views

    def handle_404(self, environ, start_response):
        from Urlencode.controllers import api
        path = environ['PATH_INFO']
        dispatcher = api.api(start_response, **environ)
        enc = dispatcher.can_dispatch(path)
        if not enc:
            return super(UrlencodeApplication, self).handle_404(environ,
                        start_response)
        result = [dispatcher.dispatch(encoded_url=enc) + '\r\n']
        return dispatcher.finalize(result)

