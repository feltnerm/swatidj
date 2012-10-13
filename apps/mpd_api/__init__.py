from hashlib import md5
from flask import Blueprint, jsonify
from apps.extensions import db, mpd_kit

from views import AlbumsAPI, ArtistsAPI, SongsAPI

from apps.helpers import register_api


api = Blueprint('mpd_api', __name__, url_prefix='/api/0.1')

register_api(api, AlbumsAPI, 'albums_api', pk="album_name", pk_type="string")
register_api(api, ArtistsAPI, 'artists_api', pk="artist_name", pk_type="string")
register_api(api, SongsAPI, 'songs_api', pk="song_name", pk_type="string")


@api.route("/command/play", methods=['POST', ])
def play():
    result = dict(status="_NONE", command='PLAY')
    try:
        mpd_kit.play()
        result['status'] = "_OK"
    except Exception, e:
        result['status'] = "_FAIL"
    return jsonify(result)


@api.route("/command/pause", methods=['POST', ])
def pause():
    result = dict(status="_NONE", command='PAUSE')
    try:
        mpd_kit.pause()
        result['status'] = "_OK"
    except Exception, e:
        result['status'] = "_FAIL"
    return jsonify(result)


@api.route("/stats/currentsong", methods=['GET', ])
def currentsong():
    result = dict(status="_NONE", command="currentsong")
    try:
        result['data'] = mpd_kit.currentsong()
        result['status'] = "_OK"
    except Exception, e:
        result['status'] = "_FAIL"
    return jsonify(result)


@api.route("/stats/stats", methods=['GET', ])
def stats():
    result = dict(status="_NONE", command="stats")
    try:
        result['data'] = mpd_kit.stats()
        result['status'] = "_OK"
    except Exception, e:
        result['status'] = "_FAIL"
    return jsonify(result)


@api.route("/stats/status", methods=['GET', ])
def status():
    result = dict(status="_NONE", command="status")
    try:
        result['data'] = mpd_kit.status()
        result['status'] = "_OK"
    except Exception, e:
        result['status'] = "_FAIL"
    return jsonify(result)


@api.route("/stats/version", methods=['GET', ])
def version():
    result = dict(status="_NONE", command="version")
    try:
        result['data'] = mpd_kit.version
        result['status'] = "_OK"
    except Exception, e:
        result['status'] = "_FAIL"
    return jsonify(result)