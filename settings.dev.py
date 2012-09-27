import os.path

# MPD
###
MPD_HOST = '192.168.1.100'
MPD_PORT = 6600

# Uploads
###
UPLOAD_MUSIC_FOLDER = '/stash/public/uploads/music'
UPLOADS_DEFAULT_DEST = '/stash/library/final'
UPLOADS_MUSIC_DEST = os.path.join(UPLOADS_DEFAULT_DEST, 'music')

# Global Settings
###
PRODUCTION = False
DEVELOPMENT = not PRODUCTION

DEBUG = not PRODUCTION
TESTING = DEBUG
ASSETS_DEBUG = DEBUG
SECRET_KEY = """\xd7\xe2\x064b\xd5\xc1N\xda \x81Q\xe5\xe5\x1cRe\xc32)\xbf\r\x80Pc\xb8\x13\x9a\xbe\x182\xe4\xd91\xc1\x0f\xcd\xbbaG"""

# MongoDB
###
MONGODB_DATABASE = 'r2djdb'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# Cache
###
CACHE_TYPE = 'null'
CACHE_DEFAULT_TIMEOUT = 300
