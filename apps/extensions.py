from flaskext.bcrypt import Bcrypt
from flaskext.cache import Cache
from flask.ext.mongokit import MongoKit
from lib.mpd_kit import MPDKit

bcrypt = Bcrypt()
cache = Cache()
db = MongoKit()
mpd_kit = MPDKit()

