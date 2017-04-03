from sanic import Sanic

def create_app():
    app = Sanic(__name__)
    from .api import api as api_blueprint
    app.blueprint(api_blueprint)
    return app

