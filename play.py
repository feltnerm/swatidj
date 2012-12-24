#!/usr/bin/env python

import os
import random
import readline
from pprint import pprint
from mpd import MPDClient
client = MPDClient()
client.connect("localhost", 6600)
from flask import *
print("Flask imported")
from app import init_app
import helpers
print("Helpers imported")
import extensions as ext
print("Extensions imported")

app = init_app('settings_dev.py')
print("app initialized")
os.environ['PYTHONINSPECT'] = 'True'

def show(obj):
    '''Show the dump of the properties of the object.'''
    pprint(vars(obj))
