#!/usr/bin/env python

import ConfigParser
import psycopg2

from eventlet import db_pool
from MicroMVC import controller

pool = None
config = None

class DBController(controller.BaseController):
    conn = None
    def __init__(self, *args, **kwargs):
        super(DBController, self).__init__(*args, **kwargs)
        self.conn = pool.get()
        print ('get')

    def finalize(self, *args, **kwargs):
        if not self.conn is None:
            pool.put(self.conn)
            print ('put')
        return super(DBController, self).finalize(*args, **kwargs)

config = ConfigParser.RawConfigParser()
config.read('site.cfg')
db_host = config.get('Database', 'host')
db_user = config.get('Database', 'user')
db_pass = config.get('Database', 'password')
pool = db_pool.ConnectionPool(psycopg2, host=db_host, database='urlencode', 
                user=db_user, password=db_pass)
