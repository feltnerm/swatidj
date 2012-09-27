from flask import Blueprint, redirect, request, current_app

from flask.ext.principal import identity_changed, Identity
from app.models import User, Guest
from app.extensions import db

users = Blueprint(__name__, 'users')


@users.route('/login', methods=['GET', 'POST'])
def login():

    if login:
        login_user(user)
        identity_changed.send(current_app._get_current_object(),
                identity=Identity(user._id))
        flash('Logged in successfully')
        return redirect(request.args.get('next') or '/')
    return render_template('login.html', form=form)


@users.route('/logout', methods=['GET', 'POST'])
def logout()
    logout_user()

    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    identity_changed.send(current_app._get_current_object(),
            identity=Guest)

    return redirect(request.args.get('next') or '/')



