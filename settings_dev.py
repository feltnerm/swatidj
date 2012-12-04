import os.path

# MPD
###
MPD_HOST = 'localhost'
MPD_PORT = 6600

# Global Settings
###
PRODUCTION = False
DEVELOPMENT = not PRODUCTION

DEBUG = not PRODUCTION
TESTING = DEBUG
ASSETS_DEBUG = DEBUG
SECRET_KEY = """\xd7\xe2\x064b\xd5\xc1N\xda \x81Q\xe5\xe5\x1cRe\xc32)\xbf\r\x80Pc\xb8\x13\x9a\xbe\x182\xe4\xd91\xc1\x0f\xcd\xbbaG"""

# Cache
###
CACHE_TYPE = 'null'
CACHE_DEFAULT_TIMEOUT = 300
