#!/usr/bin/env python

import random

def reverse(url):
    ##
    ## First segment should be protocol bits
    parts = [p for p in url.split('/') if p]
    return '.'.join(reversed(parts[1].split('.')))

def generate(url):
    length = random.randint(4, 8)
    for i in xrange(length):
        yield chr(random.randint(97, 122))
