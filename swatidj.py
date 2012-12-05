#!/usr/bin/env python

from flask import Flask
#from gevent import monkey; monkey.patch_all()
from apps.configure import init_app


app = init_app('settings_prod.py')
