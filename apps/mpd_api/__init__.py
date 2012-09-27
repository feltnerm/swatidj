from hashlib import md5
from apps.extensions import db, mpd_kit


def update_library():
    mpd_kit.iterate = True
    for item in mpd_kit.listallinfo():
        if item.get('file') is not None:
            fileid = md5(item.get('file').encode('utf')).hexdigest()
            existing_track = db.Track.find_one({'fileid': fileid})
            if existing_track:
                existing_track.update(fileid=fileid, 
                        update_time=datetime.utcnow(), **el)
                existing_track.save()
            else:
                new_track = Track(fileid=fileid, **el)
                db.tracks.insert(new_track)
    mpd_kit.iterate = False



