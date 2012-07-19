from functools import wraps
from datetime import datetime

from flask import request, Response, jsonify, abort

from flask.ext.login import LoginManager, UserMixin, AnonymousUser
from flask.ext.mongokit import Document
from flask.ext.principal import Principal, RoleNeed, UserNeed, Permission, \
        identity_loaded
from app.extensions import bcrypt, db


ROLES = {
        'guest': 0,
        'streamer': 1,
        'leecher': 2,
        'seeder': 3,
        'moderator': 4,
        'admin': 5,
        'superuser': 6
        }

superuser = Permission(RoleNeed(6))
admin = Permission(RoleNeed(5))
moderator = Permission(RoleNeed(4))
seeder = Permission(RoleNeed(3))
leecher = Permission(RoleNeed(2))
streamer = Permission(RoleNeed(1))
guest = Permission(RoleNeed(0))
null = Permission(RoleNeed(None))


class Guest(AnonymousUser):
    username = u'Guest'
    role = 0
    _id = None


class User(Document, UserMixin):


    __collection__ = 'users'
    use_dot_notation = True

    structure = {
            'username': unicode,
            'password_hash': unicode,
            'date_join': datetime,
            'last_login': datetime,
            'role': int,
    
            # Optional:
            'email': unicode
            }

    required_fields = ['username', 'password_hash', 'date_join', 'role']
    default_values = {
            'date_join': datetime.utcnow(),
            'role': 0
            }

    def create(self, username, password, active=True, role=1):
        self.username = username
        self.password_hash = unicode(bcrypt.generate_password_hash(password))
        self.active = active
        self.role = role
        self.date_created = datetime.utcnow()
         
    def check_password(self, password):
        if not self.password_hash:
            return False
        return bcrypt.check_password_hash(self.password_hash, password)

    def is_active(self):
        return self.active
    
    def is_streamer(self):
        return self['role'] >= ROLES['streamer']

    def is_leecher(self):
        return self['role'] >= ROLES['leecher']

    def is_seeder(self):
        return self['role'] >= ROLES['seeder']

    def is_moderator(self):
        return self['role'] >= ROLES['moderator']

    def is_admin(self):
        return self['role'] >= ROLES['admin']

    def provides(self):
        needs = [RoleNeed('authenticated'),
                UserNeed(self._id)]
        if self.is_streamer:
            needs.append(RoleNeed('streamer'))
        if self.is_leecher:
            needs.append(RoleNeed('leecher'))
        if self.is_seeder():
            needs.append(RoleNeed('seeder'))
        if self.is_moderator():
            needs.append(RoleNeed('moderator'))
        if self.is_admin():
            needs.append(RoleNeed('admin'))
        return needs

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
    user = db.User.find_one_or_404({'username': username})
    if user:
        authenticated = user.check_password(password)
    else:
        authenticated = False
    return user, authenticated


def init_app(app):
    """ Configure middleware for the application. """

    principal = Principal(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        user = user_from_username(identity.name) 
        identity.provides.add(RoleNeed(user.role))
        identity.user = user
        g.user = user

    db.register(User)


def user_from_userid(uid):
    return db.users.get_one_or_404(uid)


def user_from_username(username):
    return db.users.find_one_or_404({'username': username})


def username_is_unique(username):
    if db.users.find_one({'username': username}).count() >= 1:
        return False
    return True
