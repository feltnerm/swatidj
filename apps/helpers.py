from flask import jsonify, json


def register_api(app, view, endpoint, url=None, extra_methods=[], pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    if url is None and hasattr(view, 'url'):
        url = view.url
    if pk is not None:
        app.add_url_rule(url, defaults={pk: None},
                         view_func=view_func, methods=['GET', ])
        app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                         methods=['GET', ] + extra_methods)
    else:
        app.add_url_rule(url, view_func=view_func, methods=['GET', ])

    if "POST" in extra_methods:
        app.add_url_rule(url, view_func=view_func, methods=['POST', ])


def is_allowed_file(filename, allowed_set):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in allowed_set
