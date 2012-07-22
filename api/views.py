
from flask import Blueprint
from flask.views import MethodView
from flask import jsonify

from extensions import mpd

mpd_api = Blueprint('mpd_api', __name__)

@mpd_api.route('/')
def stats():
    mpd.connect()
    stats = mpd.stats()
    mpd.disconnect()
    return jsonify(stats)

