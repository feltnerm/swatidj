from hashlib import md5
from flask import Blueprint, jsonify, abort

from extensions import mpd_kit

from models import Library, Artist, Album, Song

api = Blueprint('mpd_api', __name__, url_prefix='/mpd')


@api.route("/artist")
@api.route("/artist/<artist_name>")
def artist(artist_name=None):
    if artist_name is None:
        lib = Library()
        return jsonify(lib.artists)
    else:
        artist = Artist(artist_name=artist_name)
        return jsonify(artist)


@api.route("/album")
@api.route("/album/<album_name>")
def album(album_name=None):
    if album_name is None:
        lib = Library()
        return jsonify(lib.albums)
    else:
        album = Album(album_name=album_name)
        return jsonify(album)

@api.route("/song")
@api.route("/song/<song_name>")
def song(song_name=None):
    if song_name is None:
        lib = Library()
        return jsonify(lib.songs)
    else:
        song = Song(title=song_name)
        return jsonify(song)

@api.route("/currentsong", methods=['GET', ])
def currentsong():
    result = mpd_kit.currentsong()
    return jsonify(result)


@api.route("/nextsong", methods=['GET',])
def nextsong():
    result = {}
    current_pos = int(mpd_kit.currentsong().get('pos'))
    playlist = [x for x in enumerate(mpd_kit.playlistinfo())]
    result = playlist[(current_pos + 1) % len(playlist)][1]
    return jsonify(result)

@api.route("/prevsong", methods=['GET',])
def prevsong():
    result = {}
    current_pos = int(mpd_kit.currentsong().get('pos'))
    playlist = [x for x in enumerate(mpd_kit.playlistinfo())]
    result = playlist[(current_pos - 1) % len(playlist)][1]
    return jsonify(result)

@api.route("/stats", methods=['GET', ])
def stats():
    result = mpd_kit.stats()
    return jsonify(result)


@api.route("/status", methods=['GET', ])
def status():
    result = mpd_kit.status()
    return jsonify(result)


@api.route("/version", methods=['GET', ])
def version():
    result = mpd_kit.version
    return jsonify(result)
