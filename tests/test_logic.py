#!/usr/bin/env python

import unittest

from Urlencode import logic

class ReverseDomainTests(unittest.TestCase):
    def test_long(self):
        url = '''http://www.mediaweek.co.uk/news/bulletin/mediaam/article/895884/?DCMP=EMC-MediaAMBulletin'''
        self.assertEquals(logic.rdomain(url), 'uk.co.mediaweek.www')

    def test_short(self):
        url = '''http://google.com/'''
        self.assertEquals(logic.rdomain(url), 'com.google')


class EncodingTests(unittest.TestCase):
    def runTest(self):
        self.assertTrue(logic.encoding())


if __name__ == '__main__':
    unittest.main()

