from settings.extensions import cache


def init_app(app):
    cache.init_app(app)