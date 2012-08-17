#!/usr/bin/env python

import sys
import os
import os.path
import logging
import binascii

# ================
# Server Settings
# ================

SITE_NAME = 'r2dj' #ENTER SITE NAME!

# ===
# MPD
# ===
MPD_HOST = '192.168.1.100'
MPD_PORT = 6600

# ======================
# Directory Declarations
# ======================

CURRENT_DIR = os.path.dirname(__file__)
APPS_ROOT = os.path.join(CURRENT_DIR, 'apps')
APPS_DIRS = (
        )
TEMPLATE_DIRS = (os.path.join(APPS_ROOT, 'templates'), )
STATIC_ROOT = os.path.join(APPS_ROOT, 'static')
HELPERS_ROOT = os.path.join(CURRENT_DIR, 'helpers')
VENDOR_ROOT = os.path.join(CURRENT_DIR, 'vendor')
LIB_ROOT = os.path.join(CURRENT_DIR, 'lib')

MUSIC_DIRECTORY = os.path.expanduser('~/Music')


# ===========
# Python Path
# ===========
if '/helpers' not in ''.join(sys.path):
    sys.path.append(HELPERS_ROOT)
if '/vendor' not in ''.join(sys.path):
    sys.path.append(VENDOR_ROOT)
if '/lib' not in ''.join(sys.path):
    sys.path.append(LIB_ROOT)

# ===============
# Global Settings
# ===============
PRODUCTION = False 
DEVELOPMENT = not PRODUCTION

DEBUG = not PRODUCTION
TESTING = DEBUG
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'utc'
ASSETS_DEBUG = DEBUG
INDEX_TEMPLATE = 'index.html'
SECRET_KEY = """)35b+%N(T+Jm(Cd@C8SPfq+eXhEq&BX**%NUb(34)kN,1d$BV!ZPA#)j"""

# =======
# Logging
# =======
LOG_LEVEL = logging.DEBUG
LOGGER_NAME = SITE_NAME
LOG_DIR = os.path.join(CURRENT_DIR, 'log')
LOGFILE = os.path.join(LOG_DIR, '%s.log' % SITE_NAME) # ENTER APP NAME
DEBUG_LOG = os.path.join(LOG_DIR, 'debug.log')
ERROR_LOG = os.path.join(LOG_DIR, 'error.log')

# =======
# MongoDB
# =======
MONGODB_DATABASE = 'r2dj'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_USERNAME = ''
MONGODB_PASSWORD = ''

# =====
# Cache
# =====
CACHE_TYPE = 'null'
CACHE_DEFAULT_TIMEOUT = 300
#CACHE_TYPE = 'memcached'
#CACHE_MEMCACHED_SERVERS = [os.environ.get('MEMCACHE_USERNAME')+':'+os.environ.get('MEMCACHE_PASSWORD')+'@'+os.environ.get('MEMCACHE_SERVERS'),]
