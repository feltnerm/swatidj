#!/usr/bin/env python

import os
import random
import readline
from pprint import pprint
from flask import *
from app import make_app
from app import helpers
from app.extensions import *

app = make_app('settings.dev.py')
os.environ['PYTHONINSPECT'] = 'True'

def show(obj):
    '''Show the dump of the properties of the object.'''
    pprint(vars(obj))
