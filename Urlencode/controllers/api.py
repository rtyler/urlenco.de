#!/usr/bin/env python

try:
    import yajl as json
except ImportError:
    import json

from MicroMVC import controller
from redis import Redis

class api(controller.BaseController):
    content_type = 'text/html'
    redis = None

    def __init__(self, *args, **kwargs):
        super(api, self).__init__(*args, **kwargs)
        self.redis = Redis(db='urlencode')

    def __del__(self):
        if not self.redis is None:
            self.redis.disconnect()

    @controller.action(paths=('/Post.aspx',))
    def encode(self, unencoded_url=None, redirect_type='http', **kwargs):
        return self.render('encoded', encoded='http://urlenco.de/fail')

    @controller.action(paths=('/PostJSON.aspx', '/api/encode'))
    def encode_json(self, **kwargs):
        return '/api/encode'

    @controller.action(paths=('/Dispatch.aspx',))
    def dispatch(self, encoded_url=None, **kwargs):
        if not encoded_url:
            return 'Fail'
        entry = json.loads(self.redis[encoded_url])
        if not entry.get('url'):
            return fail
        self.code = 301
        self.headers.append(('Location', entry['url'] + '\r\n'))
        return ''

    def can_dispatch(self, segment):
        pieces = segment.split('/')
        if len(pieces) > 2:
            return False
        url_enc = pieces[1]
        if self.redis.exists(url_enc):
            return url_enc
        return False
