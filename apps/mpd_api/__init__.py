from hashlib import md5
from flask import Blueprint, jsonify, abort

from apps.extensions import mpd_kit
from apps.helpers import register_api


api = Blueprint('mpd_api', __name__, url_prefix='/api')


@api.route("/playlist", methods=['GET',])
def playlist():
    result = {}
    try:
        result = [x for x in enumerate(mpd_kit.playlistinfo())]
        return jsonify(result)
    except Exception, e:
        abort(500)


@api.route("/currentsong", methods=['GET', ])
def currentsong():
    result = {}
    try:
        result = mpd_kit.currentsong()
    except Exception, e:
        abort(500)
    return jsonify(result)


@api.route("/nextsong", methods=['GET',])
def nextsong():
    result = {}
    try:
        current_pos = int(mpd_kit.currentsong().get('pos'))
        playlist = [x for x in enumerate(mpd_kit.playlistinfo())]
        result = playlist[current_pos + 1][1]
        return jsonify(result)
    except Exception, e:
        abort(500)

@api.route("/prevsong", methods=['GET',])
def prevsong():
    result = {}
    try:
        current_pos = int(mpd_kit.currentsong().get('pos'))
        playlist = [x for x in enumerate(mpd_kit.playlistinfo())]
        result = playlist[current_pos - 1][1]
        return jsonify(result)
    except Exception, e:
        abort(500)

@api.route("/stats", methods=['GET', ])
def stats():
    result = dict()
    try:
        result = mpd_kit.stats()
    except Exception, e:
        abort(500)
    return jsonify(result)


@api.route("/status", methods=['GET', ])
def status():
    result = dict()
    try:
        result = mpd_kit.status()
    except Exception, e:
        abort(500)
    return jsonify(result)


@api.route("/version", methods=['GET', ])
def version():
    result = dict()
    try:
        result = mpd_kit.version
    except Exception, e:
        abort(500)
    return jsonify(result)
