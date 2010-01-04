#!/usr/bin/env python

import math
import random

def rdomain(url):
    ''' Return the reverse domain for the url '''
    parts = url.split('/')
    protocol, domain = parts[0], parts[2]
    return '.'.join(reversed(domain.split('.')))

def encoding():
    def _gen():
        length = random.randint(4, 8)
        for i in xrange(length):
            yield chr(int(math.floor(26 * random.random() + 65)) )
    return ''.join(_gen()).lower()


