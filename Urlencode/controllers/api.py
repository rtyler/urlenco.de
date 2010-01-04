#!/usr/bin/env python

import time
try:
    import yajl as json
except ImportError:
    import json

from MicroMVC import controller
from redis import Redis

from Urlencode import logic

class api(controller.BaseController):
    content_type = 'text/html'
    redis = None

    def __init__(self, *args, **kwargs):
        super(api, self).__init__(*args, **kwargs)
        self.redis = Redis(db='urlencode')

    def __del__(self):
        if not self.redis is None:
            self.redis.disconnect()

    def _encode(self, url, http_redirect):
        encoded = logic.encoding()
        if self.redis.exists(encoded):
            while self.redis.exists(encoded):
                encoded = logic.encoded()

        rurl = logic.rdomain(url)
        data = {'url' : url, 'url_enc' : encoded, 'created' : time.time(), 
                        'flags' : 0, 'rurl' : rurl}
        # Forward mapping
        self.redis[encoded] = json.dumps(data)
        # Reverse mapping
        self.redis[url] = encoded
        return encoded


    @controller.action(paths=('/Post.aspx', '/encode',))
    def encode(self, unencoded_url=None, redirect_type='http', **kwargs):
        if not unencoded_url:
            return 'Fail'
        # Check to see if we know this already
        encoded = self.redis.get(unencoded_url)
        if not encoded:
            encoded = self._encode(unencoded_url, redirect_type == 'http')
        return self.render('encoded', encoded='http://urlenco.de/%s' % encoded)

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
