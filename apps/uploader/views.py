import os

from flask import Blueprint, render_template, current_app, request, flash

from flask.ext.uploads import AUDIO

from apps.helpers import is_allowed_file

uploader = Blueprint('uploader', __name__)


@uploader.route('/upload/', methods=['GET', 'POST',])
def upload():
    music_upload_set = current_app.upload_set_config.get('music')
    if request.method == 'POST':
        files = request.files.getlist("files[]")
        for file in files:
            if is_allowed_file(file.filename, AUDIO):
                print file.filename
    return render_template('upload.html')
