#!/usr/bin/env python

from flask import Flask, jsonify, g

from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

import auth
import extensions

from helpers import register_api


def configure_beforehandlers(app):

    @app.before_request
    def authenticate():
        g.user = getattr(g.identity, 'user', None)


def configure_errorhandlers(app):
    """ Set default error pages (404, 505, etc.). """

    def make_json_error(error):
        response = jsonify(message=str(error))
        response.status_code = (error.code
                                if isinstance(error, HTTPException)
                                else 500)
        return response

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error    
    

def configure_extensions(app):
    """ Import and init required extensions. (located in extensions.py). """

    extensions.bcrypt.init_app(app) 
    extensions.cache.init_app(app)
    extensions.db.init_app(app)
    extensions.mpd.init_app(app)
    extensions.mpd.connect(app.config['MPD_HOST'], app.config['MPD_PORT'])

    auth.init_app(app)


def configure_logging(app):
    """ Set up the application's logger. """
    pass


def configure_api(app):

    pass
    #register_api(app, api.MPDDatabaseAPI, 'database_api', '/database/', pk='command', pk_type='string')
    #register_api(app, api.MPDPlaybackAPI, 'playback_api', '/playback/', pk='command', pk_type='string')
    #register_api(app, api.AlbumAPI, 'albums_api', '/albums/', pk='album_id')
    #register_api(app, api.ArtistAPI, 'artists_api', '/artists/', pk='artist_id')
    #register_api(app, api.SongAPI, 'songs_api', '/songs/', pk='song_id')

def configure_app(app, config_filename):
    """ Configures the application. """
    app.config.from_pyfile(config_filename)
    
    def setdefault(d, key, value):
        if d.get(key) is None:
            d[key] = value

    configure_logging(app)
    configure_extensions(app)
    configure_beforehandlers(app)
    configure_errorhandlers(app)
    configure_api(app)
