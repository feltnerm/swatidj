from datetime import datetime
from hashlib import md5
from apps.extensions import mpd_kit


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
