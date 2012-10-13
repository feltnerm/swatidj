from flask import jsonify, request, abort
from flask.views import MethodView

from apps.extensions import db, mpd_kit
from models import update_library, get_library

"""
    Should represent RESTful-esque ways to talk with MPD (specifically the mpd_kit)
"""


def result_from_list(in_list, key):
    result = {}
    for e in in_list:
        if isinstance(e, dict):
            k = e.get(key, None)
        else:
            k = None
        if k in result:
            result[k].append(e)
        else:
            result[k] = [e]
    return result


def enumerate_list(in_list):
    result = {}
    print in_list
    for i, e in enumerate(in_list):
        result[i] = e
    return result


class AlbumsAPI(MethodView):

    url = "/albums/"

    def get(self, album_name=""):
        data = None
        if album_name is not None:
            data = mpd_kit.search('album', album_name)
        else:
            data = mpd_kit.list('album')
        final_data = result_from_list(data, 'album')
        return jsonify(final_data)


class ArtistsAPI(MethodView):

    url = "/artists/"

    def get(self, artist_name=""):
        if artist_name is not None:
            data = mpd_kit.search('artist', artist_name)
        else:
            data = mpd_kit.list('artist')
        final_data = result_from_list(data, 'artist')
        return jsonify(final_data)


class SongsAPI(MethodView):

    url = "/songs/"

    def get(self, song_name=""):
        if song_name is not None:
            data = mpd_kit.search('title', song_name)
        else:
            data = mpd_kit.list('title')
        final_data = enumerate_list(data)
        return jsonify(final_data)
