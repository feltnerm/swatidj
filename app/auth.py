from functools import wraps
from datetime import datetime
from flask import request, Response, abort
from flask.ext.login import LoginManager
from flask.ext.principal import Principal, identity_loaded

from extensions import bcrypt, db
from models.users import User, user_from_id, user_from_username


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response('Could not verify your access level for that URL.\n'
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return abort(401)
        user, authenticated = check_auth(auth.username, auth.password)
        if not user or not authenticated:
            return abort(401)
        return f(*args, **kwargs)
    return decorated


def check_auth(username, password):
    user = None
    authenticated = False
    if uid or username:
        user = db.User.find({'$or': [{'_id': uid}, {'username': username}]}, {'_id': 1, 'username': 1})
        if user:
            authenticated = user.check_password(password)
    return user, authenticated 


def init_app(app):
    """ Configure middleware for the application. """

    principal = Principal(app)
    login_manager = LoginManager()

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        user = user_from_id(identity._id) 
        identity.provides.add(RoleNeed(user.access_level))
        identity.user = user
        g.user = user

    @login_manager.user_loader
    def load_user(uid):
        return user_from_id(uid)


    db.register(User)
