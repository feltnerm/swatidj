from datetime import datetime
from hashlib import md5
import itertools

import simplejson as json

from extensions import mpd_kit


def dict_from_list(in_list, key):
    result = {}
    for e in in_list:
        if isinstance(e, dict):
            k = e.get(key, None)
        else:
            k = None
        if k in result:
            result[k].append(e)
        else:
            result[k] = [e]
    return result


def enumerate_list(in_list):
    result = {}
    for i, e in enumerate(in_list):
        result[i] = e
    return result

class Storage(dict):

    __slots__ = ()
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    __getattr__ = dict.get
    __getitem__ = dict.get

    def to_json(self):
        return json.dumps(self)

    def __hash__(self):
        if hasattr(self, 'file'):
            return hash(self.file)
        else:
            return hash(self.keys)

class Library(object):

    @property
    def artists(self):
        artists = set()
        for a in mpd_kit.list('artist'):
            artist = Artist(artist_name=a)
            artists.add(artist)
        return self._dictify(artists, 'artist_name')

    @property
    def albums(self):
        albums = set()
        for a in mpd_kit.list('album'):
            album = Album(album_name=a)
            albums.add(album)
        return self._enumerate(albums, 'album_name')

    @property
    def songs(self):
        songs = set()
        for s in mpd_kit.listallinfo():
            song = Song(**s)
            songs.add(song)
        return self._enumerate(songs, 'title')

    def album_by_name(self, album_name):
        return mpd_kit.find('album', album_name)

    def albums_by_artist(self, artist_name):
        return mpd_kit.list('album', artist_name)

    def song_by_name(self, song_name):
        return mpd_kit.find('track', song_name)

    def songs_by_artist(self, artist_name):
        predicate = lambda s: s if s.get('artist', None) == artist_name else None
        return filter(predicate, mpd_kit.listallinfo())

    def songs_by_album(self, album_name):
        predicate = lambda s: s if s.get('album', None) == album_name else None
        return filter(predicate, mpd_kit.listallinfo())

    def _enumerate(self, in_list):
        d = {}
        for i,v in enumerate(in_list):
            d[i] = v
        return d

    def _dictify(self, in_list, key):
        result = {}
        for e in in_list:
            if isinstance(e, dict):
                k = e.get(key, None)
            else:
                k = key 
            if k in result:
                result[k].append(e)
            else:
                result[k] = [e]
        return result

class Artist(Storage):

    def __init__(self, artist_name, *args, **kwargs):
        self.update(artist_name=artist_name)
        #self._populate()

    def get_albums(self):
        for alb in Library().albums_by_artist(self.artist_name):
            self.albums.add(Album(alb))


class Album(Storage):
    
    COVER = 'cover'

    def __init__(self, album_name, artist=None, albumartist=None, 
            songs=[], date=None, *args, **kwargs):
        self.update(album_name=album_name, songs=songs, artist=artist,
                albumartist=albumartist, date=date)
        #self._populate()

    def _populate(self):
        self.songs = Library().album_by_name(self.album_name)
        

class Song(Storage):

    def __init__(self, title=None, album=None, track=None, file=None, 
            time=None, genre=None, date=None, disc=None, *args, **kwargs):
        self.update(title=title, album=album, track=track, file=file,
                time=time, genre=genre, date=date, disc=disc)

        #self._populate()

    def _populate(self):
        info = None 
        if self.file:
            info = mpd_kit.find('file', self.file)
        elif self.title:
            info = mpd_kit.find('title', self.title)

        for k, v in info[0].iteritems():
            if self.has_key(k):
                self[k] = v

