
from flask.views import MethodView
from flask import jsonify, request

from extensions import mpd


class MPDMethodView(MethodView):

    def get(self):
        result = mpd.status()
        return jsonify(result)
        #return jsonify(getattr(mpd, command, None)) 

    def post(self):
        args = request.args
        if command is None:
            return jsonify(result=None)
            #return jsonify(mpd.status())
        return jsonify(command=command,
                args=args)
        #return jsonify(mpd.__getattribute__(command)()) 

