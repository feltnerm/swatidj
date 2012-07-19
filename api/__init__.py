#!/usr/bin/env python

import sys
from flask import Flask
from logbook.compat import redirect_logging
from api import configure

def make_app(config=None):
    redirect_logging()
    app = Flask(__name__)
    configure.configure_app(app, config)
    
    return app
