from flask import jsonify, request, abort
from flask.views import MethodView

from apps.extensions import db, mpd_kit
from models import mpd_search, mpd_list

"""
    Should represent RESTful-esque ways to talk with MPD (specifically the mpd_kit)
"""


class AlbumsAPI(MethodView):

    url = "/albums/"

    def get(self, album_name=""):
        data = None
        if album_name is not None:
            data = mpd_search('album', album_name)
        else:
            data = mpd_list('album')
        return jsonify(data)


class ArtistsAPI(MethodView):

    url = "/artists/"

    def get(self, artist_name=""):
        if artist_name is not None:
            data = mpd_search('artist', artist_name)
        else:
            data = mpd_list('artist')
        return jsonify(data)


class SongsAPI(MethodView):

    url = "/songs/"

    def get(self, song_name=""):
        if song_name is not None:
            data = mpd_search('title', song_name)
        else:
            data = mpd_list('title')
        return jsonify(data)
