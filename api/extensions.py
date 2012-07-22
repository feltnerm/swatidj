from flaskext.bcrypt import Bcrypt
from flaskext.cache import Cache
from flask.ext.mongokit import MongoKit
import mpd_kit

bcrypt = Bcrypt()
cache = Cache()
db = MongoKit()
mpd = mpd_kit.MPD()
