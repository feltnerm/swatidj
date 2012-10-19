from hashlib import md5
from flask import Blueprint, jsonify, abort
from apps.extensions import db, mpd_kit

from views import AlbumsAPI, ArtistsAPI, SongsAPI

from apps.helpers import register_api


api = Blueprint('mpd_api', __name__, url_prefix='/api/0.1')

register_api(api, AlbumsAPI, 'albums_api', pk="album_name", pk_type="string")
register_api(api, ArtistsAPI, 'artists_api', pk="artist_name", pk_type="string")
register_api(api, SongsAPI, 'songs_api', pk="song_name", pk_type="string")


@api.route("/command/play/", methods=['POST', ])
def play():
    result = {}
    try:
        mpd_kit.play()
        result['status'] = "_OK"
    except Exception, e:
        result['status'] = "_FAIL"
    return jsonify(result)


@api.route("/command/pause/", methods=['POST', ])
def pause():
    result = {}
    try:
        mpd_kit.pause()
    except Exception, e:
        abort(500)
    return jsonify(result)


@api.route("/stats/currentsong/", methods=['GET', ])
def currentsong():
    result = dict()
    try:
        result = mpd_kit.currentsong()
    except Exception, e:
        abort(500)
    return jsonify(result)


@api.route("/stats/stats/", methods=['GET', ])
def stats():
    result = {}
    try:
        result = mpd_kit.stats()
    except Exception, e:
        abort(500)
    return jsonify(result)


@api.route("/stats/status/", methods=['GET', ])
def status():
    result = {}
    try:
        result = mpd_kit.status()
    except Exception, e:
        abort(500)
    return jsonify(result)


@api.route("/stats/version/", methods=['GET', ])
def version():
    result = {}
    try:
        result = mpd_kit.version
    except Exception, e:
        abort(500)
    return jsonify(result)