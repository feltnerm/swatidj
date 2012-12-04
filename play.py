#!/usr/bin/env python

import os
import random
import readline
from pprint import pprint
from flask import *
print("Flask imported")
from apps.configure import init_app
from apps import helpers
print("Helpers imported")
from apps.extensions import *
print("Extensions imported")

app = init_app('settings_dev.py')
print("app initialized")
os.environ['PYTHONINSPECT'] = 'True'

def show(obj):
    '''Show the dump of the properties of the object.'''
    pprint(vars(obj))
