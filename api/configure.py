#!/usr/bin/env python

from flask import Flask, jsonify, g

from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

import auth
import extensions
import api

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
    auth.init_app(app)


def configure_logging(app):
    """ Set up the application's logger. """
    pass


def configure_api(app):

    mpdapi_view = api.MPDMethodView.as_view('mpd_api')
    app.add_url_rule('/api', view_func=mpdapi_view, methods=['GET','POST'])

def configure_app(app, config_filename):
    """ Configures the application. """
    app.config.from_pyfile(config_filename)
    
    def setdefault(d, key, value):
        if d.get(key) is None:
            d[key] = value

    configure_logging(app)

    app.logger.debug(app.config)

    configure_extensions(app)
    configure_beforehandlers(app)
    configure_errorhandlers(app)
    configure_api(app)
