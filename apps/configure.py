#!/usr/bin/env python
import os.path
from flask import Flask, jsonify, g, render_template

from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

from flask.ext.uploads import UploadSet, AUDIO, IMAGES, configure_uploads, \
        patch_request_class
import auth
import extensions

from helpers import register_api
from uploader.views import uploader
from mpd_api.views import Controller, Playlist, Library


def init_frontend(app):

    @app.route('/')
    def index():
        return render_template('index.html')


def init_apis(app):
    
    # Control API
    register_api(app, view=Controller, endpoint='mpd_controller', 
           url='/api/0.1/c/', pk=None)  

    # Library APi
    register_api(app, view=Library, endpoint='mpd_database',
           url='/api/0.1/library/', pk=None)

    # Playlist API
    register_api(app, view=Playlist, endpoint='mpd_playlist', 
           url='/api/0.1/playlist/', pk='playlist_id', pk_type='int')

    # Uploads
    app.register_blueprint(uploader)


def init_beforehandlers(app):

    @app.before_request
    def authenticate():
        g.user = getattr(g.identity, 'user', None)


def init_errorhandlers(app):
    """ Set default error pages (404, 505, etc.). """

    def make_json_error(error):
        response = jsonify(message=str(error))
        response.status_code = (error.code
                                if isinstance(error, HTTPException)
                                else 500)
        return response

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error    
    

def init_extensions(app):
    """ Import and init required extensions. (located in extensions.py). """

    extensions.bcrypt.init_app(app) 
    extensions.cache.init_app(app)
    extensions.db.init_app(app)
    extensions.mpd_kit.init_app(app)

    auth.init_app(app)

def init_uploads(app):
    music_upload_set = UploadSet(name='music', extensions=AUDIO,
            default_dest=lambda app: app.config['UPLOADS_MUSIC_DEST'])
    configure_uploads(app, (music_upload_set,))
    patch_request_class(app, 32 * 1024 * 1024 * 100)


def init_app(config):
    """ Configures the application. """
    
    app = Flask(__name__)

    app.config.from_pyfile(os.path.abspath('settings.defaults.py'))
    try:
        app.config.from_pyfile(os.path.abspath(config))
    except IOError, e:
        print e

    init_extensions(app)
    init_beforehandlers(app)
    init_errorhandlers(app)
    init_apis(app)
    init_frontend(app)
    init_uploads(app)
    return app

