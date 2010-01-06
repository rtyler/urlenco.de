#!/usr/bin/env python

import time
import urllib
try:
    import yajl as json
except ImportError:
    import json

from MicroMVC import controller
from redis import Redis

from Urlencode import logic

class api(controller.BaseController):
    redis = None

    def __init__(self, *args, **kwargs):
        super(api, self).__init__(*args, **kwargs)
        self.redis = Redis(db='urlencode')
        self.content_type = 'text/html'

    def __del__(self):
        if not self.redis is None:
            self.redis.disconnect()

    def _encode(self, url, http_redirect=True):
        encoded = self.redis.get(url)
        if encoded:
            return 'http://urlenco.de/%s' % encoded
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
        return 'http://urlenco.de/%s' % encoded

    @controller.action(paths=('/Post.aspx', '/encode',))
    def encode(self, unencoded_url=None, redirect_type='http', **kwargs):
        if not unencoded_url:
            return 'Fail'

        unencoded_url = urllib.unquote(unencoded_url)
        encoded = self._encode(unencoded_url, redirect_type == 'http')
        return self.render('encoded', encoded=encoded)

    def encode_json(self, encode=None, **kwargs):
        if not encode:
            return {}
        encoded = self._encode(encode)
        return {'url' : encode, 'encoded' : encoded}

    def decode_json(self, decode=None, **kwargs):
        if not decode:
            return {}
        piece = decode.split('/')[-1]
        entry = self.redis[piece]
        if not entry:
            return {}
        entry = json.loads(entry)
        return {'url' : entry['url'], 'encoded' : 'http://urlenco.de/%s' % piece}

    @controller.action(paths=('/PostJSON.aspx', '/api'))
    def api(self, **kwargs):
        self.content_type = 'text/plain'
        if kwargs.get('encode'):
            return json.dumps(self.encode_json(**kwargs))
        if kwargs.get('decode'):
            return json.dumps(self.decode_json(**kwargs))
        return '{}'


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
