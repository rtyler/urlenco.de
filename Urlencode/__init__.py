#!/usr/bin/env python

import ConfigParser
import logging

import psycopg2
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
