from flask import jsonify, request, abort
from flask.views import MethodView

from apps.extensions import mpd_kit

"""
    Should represent RESTful-esque ways to talk with MPD (specifically the mpd_kit)
"""

