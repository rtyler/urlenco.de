#!/usr/bin/env python

import unittest

from Urlencode import encoder

class ReverseDomainTests(unittest.TestCase):
    def test_google(self):
        rc = encoder.reverse('http://www.google.com/')
        self.assertEquals(rc, 'com.google.www')

    def test_long_url(self):
        rc = encoder.reverse('http://www.google.com/analytics/')
        self.assertEquals(rc, 'com.google.www')


class RandomizeTests(unittest.TestCase):
    def test_google(self):
        rc = encoder.generate('http://www.google.com')
        print ('rc', ''.join(rc))



if __name__ == '__main__':
    unittest.main()

