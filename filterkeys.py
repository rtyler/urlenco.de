#!/usr/bin/env python

import pprint
import sys

import redis
import yajl

def main():
    lines = [l.strip() for l in sys.stdin.xreadlines()]
    r = redis.Redis()
    keys = r.keys().split(' ')

    assert r.dbsize() == len(keys), (len(keys), 'Not enough keys!')

    print '>>> Exactly %d keys to iterate through' % len(keys)

    for line in lines:
        if not line:
            continue
        print '>> Filtering %s' % line

        matches = []
        for key in keys:
            value = None
            try:
                value = yajl.loads(r.get(key))
                if not value.get('url'):
                    continue

                if value['url'].find(line) >= 0:
                    matches.append(key)

            except ValueError:
                pass

        print '>>> Found %d bad keys' % len(matches)
        for badkey in matches:
            r.delete(badkey)
    return 0

if __name__ == '__main__':
    exit(main())

