import logging
import os
import os.path
import sys

### DEFAULT SETTINGS ###

# Server Settings
###
SITE_NAME = 'swatidj'

# Directory Declarations
###
CURRENT_DIR = os.path.dirname(__file__)
APIS_ROOT = os.path.join(CURRENT_DIR, 'apis')
APPS_ROOT = os.path.join(CURRENT_DIR, 'apps')
LIB_ROOT = os.path.join(CURRENT_DIR, 'lib')
EXTENSIONS_ROOT = os.path.join(CURRENT_DIR, 'extensions')

TEMPLATE_DIRS = (os.path.join(APPS_ROOT, 'templates'), )
STATIC_ROOT = os.path.join(APPS_ROOT, 'static')

# Pythonpath
###
if '/lib' not in ''.join(sys.path):
    sys.path.append(LIB_ROOT)
if '/extensions' not in ''.join(sys.path):
    sys.path.append(EXTENSIONS_ROOT)

# Logging
###
LOG_LEVEL = logging.DEBUG
LOGGER_NAME = SITE_NAME
LOG_DIR = os.path.join(CURRENT_DIR, 'log')
LOG_FILE = os.path.join(LOG_DIR, '%s.log' % LOGGER_NAME)
