from flaskext.bcrypt import Bcrypt
from flaskext.cache import Cache
from flask.ext.mongokit import MongoKit
import mpd

mpd_client = mpd.MPDClient()
bcrypt = Bcrypt()
cache = Cache()
db = MongoKit()
