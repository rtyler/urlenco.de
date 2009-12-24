#!/usr/bin/env python

import sys

import MicroMVC
import Urlencode

def main():
    app = Urlencode.UrlencodeApplication()
    return MicroMVC.run(app.run)

if __name__ == '__main__':
    sys.exit(main())

