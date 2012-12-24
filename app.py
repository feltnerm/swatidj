#!/usr/bin/env python
import os.path
from flask import Flask, abort, jsonify, g, render_template

from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

#import auth
import extensions

from apis import mpd


def init_frontend(app):

    @app.route('/')
    def index():
        abort(501)


def init_apis(app):

    app.register_blueprint(mpd.api)


def init_beforehandlers(app):
    pass
    #@app.before_request
    #def authenticate():
    #    g.user = getattr(g.identity, 'user', None)


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

    #extensions.cache.init_app(app)
    extensions.mpd_kit.init_app(app)

    #auth.init_app(app)


def init_app(config):
    """ Configures the application. """

    app = Flask(__name__)

    app.config.from_pyfile(os.path.abspath('settings_default.py'))
    try:
        app.config.from_pyfile(os.path.abspath(config))
    except IOError, e:
        print e

    init_extensions(app)
    init_beforehandlers(app)
    init_errorhandlers(app)
    init_apis(app)
    init_frontend(app)
    return app
