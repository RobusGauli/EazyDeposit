import os
import sys
from sanic import Sanic

def create_app():
    app = Sanic(__name__)

    #register the API routes
    from .api import api as api_blueprint
    app.blueprint(api_blueprint)
   
    return app

