#!/usr/bin/env python

import sys
import os
import os.path
import logging
import binascii

# ================
# Server Settings
# ================

SITE_NAME = 'DJ Embe' #ENTER SITE NAME!

SUPER_USER = 'mark'
SUPER_USER_PASS = 'spanky'

# ===
# MPD
# ===
MPD_HOST = 'localhost'
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

UPLOAD_DIRECTORY = os.path.expanduser('~/music/uploads')

# ===========
# Python Path
# ===========
if '/helpers' not in ''.join(sys.path):
    sys.path.append(HELPERS_ROOT)
if '/vendor' not in ''.join(sys.path):
    sys.path.append(VENDOR_ROOT)

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
SECRET_KEY = """UHdCd[Mkaj@FH-GS#B@&SB4,9XkG%ff9m@@"pRG0N[d@d`$f-K5j2%p3"""

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
MONGODB_DATABASE = 'djembe_db'
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
