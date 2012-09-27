import logging
import os
import os.path
import sys

### DEFAULT SETTINGS ###

# Server Settings
###
SITE_NAME = 'r2dj'

# Directory Declarations
###
CURRENT_DIR = os.path.dirname(__file__)
API_ROOT = os.path.join(CURRENT_DIR, 'api')
LIB_ROOT = os.path.join(CURRENT_DIR, 'lib')
# needed?
TEMPLATE_DIRS = (os.path.join(API_ROOT, 'templates'), )
STATIC_ROOT = os.path.join(API_ROOT, 'static')


# Pythonpath
###
if '/lib' not in ''.join(sys.path):
    sys.path.append(LIB_ROOT)

# Babel
###
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'utc'

# Logging
###
LOG_LEVEL = logging.DEBUG
LOGGER_NAME = SITE_NAME
LOG_DIR = os.path.join(CURRENT_DIR, 'log')
LOG_FILE = os.path.join(LOG_DIR, '%s.log' % LOGGER_NAME)
