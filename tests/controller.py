#!/usr/bin/env python

import unittest

from Urlencode import controllers


class BaseController_QueryStringTests(unittest.TestCase):
    def objectWithQS(self, qs):
        return controllers.BaseController(None, REQUEST_METHOD='GET', QUERY_STRING=qs)

    def test_noqs(self):
        bc = self.objectWithQS('')
        self.assertEquals(bc.args, {})

    def test_one(self):
        bc = self.objectWithQS('foo=bar')
        self.assertEquals(bc.args.get('foo'), 'bar')

    def test_two(self):
        bc = self.objectWithQS('foo=bar&one=more')
        self.assertEquals(bc.args.get('one'), 'more')
        self.assertEquals(bc.args.get('foo'), 'bar')

    def test_empty(self):
        bc = self.objectWithQS('foo=')
        self.assertEquals(bc.args.get('foo'), '')

    def test_dupes(self):
        bc = self.objectWithQS('foo=1&foo=2')
        self.assertEquals(bc.args.get('foo'), ['1', '2'])

if __name__ == '__main__':
    unittest.main()

