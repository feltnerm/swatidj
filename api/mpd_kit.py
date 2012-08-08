
from flask import _request_ctx_stack
import mpd
from mpd import MPDClient

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

ctx_stack = stack


class MPD(MPDClient):

    def __init__(self, app=None, use_unicode=True, *args, **kwargs):

        super(MPD, self).__init__(use_unicode=use_unicode, *args, **kwargs)

        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None
        

    def init_app(self, app, *args, **kwargs):
        app.config.setdefault('MPD_HOST', 'localhost')
        app.config.setdefault('MPD_PORT', 6600)
        app.config.setdefault('MPD_CONFIG', '/etc/mpd.conf')
        app.config.setdefault('MPD_USERNAME', None)
        app.config.setdefault('MPD_PASSWORD', None)

        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self._teardown_request)
        elif hasattr(app, 'teardown_request'):
            app.teardown_request(self._teardown_request)
        else:
            app.after_request(self._teardown_request)

        app.extensions = getattr(app, 'extensions', {})
        app.extensions['mpd'] = self

    def connect(self):

        ctx = ctx_stack.top
        mpd_connection = getattr(ctx, 'mpd_connection', None)

        if mpd_connection is None:
            # Connect to MPD here
            ctx.mpd_connection = super(MPD, self).connect(
                    host=ctx.app.config.get('MPD_HOST'),
                    port=ctx.app.config.get('MPD_PORT'),
                    )

    @property
    def connected(self):
        ctx = ctx_stack.top
        return getattr(ctx, 'mpd_connection', None) is not None

    def disconnect(self):
        if self.connected:
            ctx = ctx_stack.top
            ctx.mpd_connection.disconnect()
            del ctx.mpd_connection

    
    def _teardown_request(self, response):
        self.disconnect()
        return response

    def __getattr__(self, name, **kwargs):
        if not self.connected:
            self.connect()

        mpd_connection = getattr(ctx_stack.top, 'mpd_connection')
        return getattr(mpd_connection, name)
