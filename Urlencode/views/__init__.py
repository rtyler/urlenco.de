#!/usr/bin/env python
from __future__ import with_statement

import os
import sys

from Cheetah import Template

# List of templates we don't want serve-able
exclude = ('base',)

def __mapTemplates():
    template_dir = os.path.dirname(__file__)

    ##
    ## NOTE: This is hackish, but will do for now
    cwd = os.getcwd()
    try:
        os.chdir(template_dir)
        if not os.getenv('NOCOMPILE'):
            os.system('cheetah compile *.tmpl')
    finally:
        os.chdir(cwd)

    for template in os.listdir(template_dir):
        if not template.endswith('.tmpl'):
            continue

        name = template.replace('.tmpl', '')

        if name in exclude:
            continue

        __import__('Urlencode.views.%s' % name)
        module = sys.modules.get('Urlencode.views.%s' % name)
        yield (name, getattr(module, name, None))

views = dict(__mapTemplates())

def get(name, default=None):
    return views.get(name, default)

def keys():
    return views.keys()


