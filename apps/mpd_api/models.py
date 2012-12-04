from datetime import datetime
from hashlib import md5
from apps.extensions import db, mpd_kit


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


def mpd_search(key, value):
    """ Fuzzy search. """
    data = dict()
    try:
        data = dict_from_list(mpd_kit.search(key, value), key)
    except Exception, e:
        data = None
    return data


def mpd_find(key, value):
    """ Exact search. """
    data = dict()
    try:
        data = dict_from_list(mpd_kit.find(key, value), key)
    except Exception, e:
        data = None
    return data


def mpd_list(key):
    data = dict()
    try:
        data = enumerate_list(mpd_kit.list(key))
    except Exception, e:
        data = None
    return data

def mpd_playlist_info():
    data = dict()
    try:
        data = dict_from_list(mpd_kit.playlistinfo(), 'pos')
    except Exception, e:
        data = None
    return data

