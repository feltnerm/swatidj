#!/usr/bin/env python

import argparse
import os
import os.path
import sys
from pprint import pprint

from flask import Flask
#from gevent import monkey; monkey.patch_all()
from app import init_app

def parse_args(args_list):
    
    ap = argparse.ArgumentParser()

    ap.add_argument('debug', action='store_true', default=False)
    ap.add_argument('--host', default='0.0.0.0')
    ap.add_argument('-p', '--port', default=5000)
    ap.add_argument('-c', '--config', default='settings_prod.py')
    args = ap.parse_args(args_list)
    return args
    

def main(argv=None):

    if not argv:
        argv = sys.argv[1:]
    options = parse_args(argv)

    swatidj = init_app(options.config)
    conf = swatidj.config.copy()
    pprint(conf, indent=2, width=80)
    swatidj.run(host=options.host, port=options.port)

    return 0 # success!


if __name__ == '__main__':

    status = main()
    sys.exit(status)

else:

    options = parge_args(sys.argv[1:])
    swatidj = init_app(options.config)
    

