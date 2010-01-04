#!/usr/bin/env python

import ConfigParser
import json
import psycopg2
import redis
import time
import urllib


def main():
    config = ConfigParser.RawConfigParser()
    config.read(('default.cfg', 'local.cfg',))
    db_host = config.get('Database', 'host')
    db_user = config.get('Database', 'user')
    db_pass = config.get('Database', 'password')

    conn = psycopg2.connect(host=db_host, user=db_user, password=db_pass)
    rconn = redis.Redis(db='urlencode')
    rconn.connect()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM urlurlurl')
        results = cursor.fetchall()
        for result in results:
            _id, url, enc, rurl, created, flags = result
            created = time.mktime(created.utctimetuple())
            # Forward mapping
            rconn[enc] = json.dumps({'url' : url, 'rurl' : rurl, 'created' : created, 'flags' : flags})
            # Reverse mapping
            url = urllib.quote_plus(url)
            rconn[url] = enc
    finally:
        conn.close()
        rconn.disconnect()

if __name__ == '__main__':
    main()

