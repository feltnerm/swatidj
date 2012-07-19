
from flask.views import MethodView
from flask import jsonify

from app.extensions import mpd_client as mpd

class MPDControl(MethodView):

    def get(self):
        return jsonify(status='GET')
    def play(self):
        mpd.play()
        return jsonify(status='play')

    def post(self):
        return jsonify(status='post')
    def pause(self):
        mpd.pause()
        return jsonify(status='pause')

    def stop(self):
        mpd.stop()
        return jsonify(status='stop')

    def fwd(self):
        mpd.next()
        return jsonify(status='fwd')

    def prev(self):
        mpd.prev()
        return jsonify(status='prev')






