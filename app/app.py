import os
from flask import Flask, request, flash, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

def build_json_app(name, **kwargs):
    """ 
    Creates a json api flask app. From http://flask.pocoo.org/snippets/83/
    """
    def make_json_error(ex):
        response = jsonify(message = str(ex))
        response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
        return response

    app = Flask(name, **kwargs)

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error

    return app

app = build_json_app("video_api")

import video_router
