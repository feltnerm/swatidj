
from datetime import datetime
from flask.ext.login import AnonymousUser
from flask.ext.mongokit import Document
from flask.ext.principal import Principal, RoleNeed, UserNeed, Permission
from app.extensions import bcrypt, db

'''
Description of access levels:
Any access level can do anything that an ACL below it can do.

    Superuser   - can do anything, basically
    Admin       - add/remove users
    Moderator   - Move uploaded tunes to library
    Seeder      - Allowed to upload tracks
    Leecher     - Allowed to download tracks
    Streamer    - Allowed to stream tracks
    Guest       - Whatever you want?
    Null        - You don't exist, you can't do shit.
'''
ACCESS_LEVELS = {
        'superuser':  (60, Permission(RoleNeed(60))),
        'admin': (50, Permission(RoleNeed(50))),      
        'moderator': (40, Permission(RoleNeed(40))),
        'seeder': (30, Permission(RoleNeed(30))), 
        'leecher': (20, Permission(RoleNeed(20))),
        'streamer': (10, Permission(RoleNeed(10))),
        'guest': (0, Permission(RoleNeed(0))),
        'null': (None, Permission(RoleNeed(None))),
        }

def user_from_id(uid):
    return db.User.find_one({'_id': uid})
def user_from_username(username):
    return db.User.find_one({'username': username})
def username_is_unique(username):
    if user_from_username(username) is not None:
        return False
    return True


# @TODO: Handle errors for non-unique username
def create_new_user(username, password, *args, **kwargs):

    user = None
    if username_is_unique(username):
        user = db.User()
        user.username = username
        user.set_password_hash(password)
    return user
    

class Guest(AnonymousUser):
    username = u'Guest'
    access_level = 0
    _id = None


class User(Document):

    __collection__ = 'users'
    use_dot_notation = True

    structure = {
            # Required
            'username': unicode,
            'password_hash': unicode,
            'access_level': int,
            'created': datetime,
            'authenticated': bool,
            'last_login': datetime,

            # Optional
            'full_name': unicode,
            'email': unicode,

            # Custom Things (to be implemented) 
            'favorite_songs': [],
            'favorite_albums': [],
            'favorite_artists': [],

            'playlists': [],

            'preferences': {}
            }
    required_fields = ['username', 'password_hash', 'access_level', 'created']
    default_values = {
            'access_level': 10,
            'created': datetime.utcnow,
            'authenticated': True, # change to false if there is going to be
                                   # some sort of email activation scheme.
            }

    ## Authn/z
    def check_password(self, potential_password):
        if not self.password_hash:
            return False
        return bcrypt.check_password_hash(self.password_hash, potential_password)

    def set_password(self, potential_password):
        self.password_hash = self.gen_passwd_hash(potential_password)

    @staticmethod
    def gen_passwd_hash(potential_password):
        return unicode(bcrypt.generate_hash(potential_password))

    ## Flask-Login required methods
    def get_id(self): return self._id
    def is_active(self): return self.active
    def is_anonymous(self): return False
    def is_authenticated(self): return self.authenticated

    def is_superuser(self): return self.access_level >= ACCESS_LEVELS['superuser'][0]
    def is_admin(self): return self.access_level >= ACCESS_LEVELS['admin'][0]
    def is_moderator(self): return self.access_level >= ACCESS_LEVELS['moderator'][0]
    def is_seeder(self): return self.access_level >= ACCESS_LEVELS['seeder'][0]
    def is_leecher(self): return self.access_level >= ACCESS_LEVELS['leecher'][0]
    def is_streamer(self): return self.access_level >= ACCESS_LEVELS['streamer'][0]

    def provides(self):
        needs = [RoleNeed('authenticated'),
                 UserNeed(self._id)]

        if self.is_streamer(): 
            needs.append(RoleNeed('streamer'))
        if self.is_leecher(): 
            needs.append(RoleNeed('leecher'))
        if self.is_seeder():
            needs.append(RoleNeed('seeder'))
        if self.is_moderator():
            needs.append(RoleNeed('moderator'))
        if self.is_admin():
            needs.append(RoleNeed('admin'))
        if self.is_superuser():
            needs.append(RoleNeed('superuser'))
        return needs 
