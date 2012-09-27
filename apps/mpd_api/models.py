from datetime import datetime
from hashlib import md5
from flask.ext.mongokit import Document
from apps.extensions import db, mpd_kit


@db.register
class Library(Document):
    __collection__ = 'library'
    use_dot_notation = True
    use_autorefs = True

    structure = {
            'revision': int,
            'last_updated': datetime 
            }
    required_fields = ['revision', 'last_updated']


def update_library():
    mpd_kit.update()
    mpd_kit.iterate = True
    for item in mpd_kit.listallinfo():
        if item.get('file') is not None:
            fileid = md5(item.get('file').encode('utf')).hexdigest()
            existing_track = db.Track.find_one({'fileid': fileid})
            if existing_track:
                existing_track.update(updated_time=unicode(datetime.utcnow().isoformat()), **item)
                existing_track.save()
            else:
                new_track = Track()
                new_track.update(fileid=fileid, **item)
                db.tracks.insert(new_track)
    mpd_kit.iterate = False


def get_library(page=1, limit=0):
    cursor = db.Track.find().skip((page-1)*limit).limit(limit)
    result = []
    return [track.to_json() for track in cursor]


@db.register
class Track(Document):

    __collection__ = 'tracks'
    use_dot_notation = True
    use_autorefs = True

    structure = {
            # tags
            'title': unicode,
            'album': unicode,
            'albumartist': unicode,
            'artist': unicode,
            'date': unicode,
            'disc': unicode,
            'track': unicode,
            'genre': unicode,
            'time': unicode,
            'file': unicode,
            'fileid': unicode,

            'bitrate': unicode,
            'filetype': unicode,

            # meta-info
            'added_time': unicode,
            'updated_time': unicode,
            'rating': int,
            'tags': [],
        }

    required_fields = ['file', 'fileid']
    default_values = {'added_time': datetime.utcnow().isoformat(), 'rating': 0}

db.register([Library, Track])
