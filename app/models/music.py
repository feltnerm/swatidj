from datetime import datetime
from flask.ext.mongokit import Document
from app.extensions import db, mpd

class Song(Document):

    __collection__ = 'songs'
    use_dot_notation = True

    structure = {
            # required
            'file': unicode,

            # tags
            'title': unicode,
            'bitrate': int,
            'track': int,

            # meta-info
            'added_time': datetime,
            'updated_time': datetime,
            'filetype': unicode,
            'rating': int,
            'tags': [],
            }

class Album(Document):

    __collection__ = 'albums'
    use_dot_notation = True
    use_autorefs = True

    structure = {
            # required
            'path': unicode,

            # tags
            'albumartist': unicode,
            'title': unicode,
            'date': datetime,
            'disc': int,

            # meta-info
            'rating': int,

            'songs': [Song]
            }

class Artist(Document):

    __collection__ = 'artists'
    use_dot_notation = True
    use_autorefs = True

    structure = {
            'name': unicode,
            'albums': [Album]
            }

class Catalog(Document):

    __collection__ = 'catalogs'
    use_dot_notation = True
    use_autorefs = True

    structure = {
            'name': unicode,
            'path': unicode,
            'last_update': datetime,
            'last_clean': datetime,
            'last_add': datetime,
            }

class Playlist(Document):

    __collection__ = 'playlists'
    use_dot_notation = True
    use_autorefs = True

    structure = {
            'name': unicode,
            'user': ObjectId(),
            'songs': [Song],
            'public': bool,
            }

