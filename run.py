#!/usr/bin/env python

import os
import sys
import argparse

from app import make_app

def main(argv=None):
    ''' Main function to run the server '''

    if not argv:
        argv = 'settings.dev.py'
    config = os.path.abspath(argv)
    
    app = make_app(config)

    if app.debug:
        app.run('0.0.0.0')
    else:
        app.run()
    
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
