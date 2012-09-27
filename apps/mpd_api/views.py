from flask import jsonify, request
from flask.views import MethodView

from apps.extensions import db, mpd_kit
from models import update_library, get_library

"""
    Should represent RESTful-esque ways to talk with MPD (specifically the mpd_kit)
"""

def make_result_response(command='', args=[], data=None,
        success=None, error=None):

    result_response = {
            'command': command, 'success':success,
            'error': { 
                'message': '',
                'error': None,
                },
            'args': args,
            'result': {
                'data': data,
                'length': 0,
                },
        }
    
    if args:
        result_response['args'] = args
    if data:
        result_response['result']['data'] = data
        if isinstance(data, dict) or isinstance(data, list):
            result_response['result']['length'] = len(data)
    if error:
        result_response['error']['message'] = error.message

    return result_response


class Controller(MethodView):

    def get(self):
        command = request.args.get('cmd')

        response_data = make_result_response(command=command)

        if command == 'status':
            result = mpd_kit.status()
            response_data['result']['data'] = result
            response_data['success'] = True
        return jsonfiy(response_data)

    def post(self):
        COMMANDS = ('play','pause','stop','next','prev')
        command = request.args.get('cmd')

        response_data = make_result_response(command=command)
        if hasattr(mpd_kit, command):
            getattr(mpd_kit, command)()
            
            response_data['command'] = command
            response_data['success'] = True

        else:
            response_data['success'] = False
            response_data['error']['message'] = 'Command not found.'
        return jsonify(response_data)


class Library(MethodView):

    def get(self):
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 50)
        sort_by = request.args.get('sort_by', 'artist')
        sort_ord = request.args.get('sort_ord', 1)

        response_data = make_result_response('GET-library')
        #try:
        data = get_library(int(page), int(limit))
        response_data['result']['data'] = data
        response_data['result']['length'] = len(data)
        response_data['success'] = True
        #except Exception, e:
        #    response_data['success'] = False
        return jsonify(response_data)


    def post(self):
        command = request.args.get('cmd')

        response_data = make_result_response(command) 

        try:
            if command == 'update':
                update_library()
            response_data['success'] = True
        except Exception, e:
            response_data['success'] = False
            response_data['error']['message'] = "%s" % e.message
        return jsonify(response_data)


class Playlist(MethodView):

    def get(self, playlist_id=None):
        if playlist_id is None:
            try:
                playlist=mpd_kit.playlistinfo()
                return jsonify(playlist=playlist,
                        success=True)
            except:
                return jsonify(playlist=None,
                        success=False)
        else:
            return jsonify(playlist=None,
                    success=False)


