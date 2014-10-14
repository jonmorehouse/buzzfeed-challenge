from flask import request, jsonify

from app import app
import action_handler
from exceptions import *

@app.route('/video/guess', methods=['POST'])
def create():
    
    if not request.headers['Content-Type'] == 'application/json':
        return "Invalid request content-type", 400, {'Content-Type': 'text/Plain'}
    
    # generate parameters to create the video
    params = {
        "title": request.json.get("title"),
        "pub": request.json.get("pub"),
        "duration": request.json.get("duration"),
    }

    # create the video and handle accordingly
    try:
        res = action_handler.action_handler("create", **params)
        return "%s => %s" % (str(params), str(res)), 201, {'Content-Type': 'text/Plain'}
    except ParamMissing:
        return "%s => Missing Params" % str(params), 400, {'Content-Type': 'text/Plain'}
    except:
        return "%s => Already exists" % params.get("title"), 400, {'Content-Type': 'text/Plain'}

@app.route('/video/guess/<title>', methods=['GET'])
def guess(title):
    res = action_handler.action_handler("find", search = title)
    # no match found
    if not res:
        return "No matches found for %s" % title
    msg = "%s => %s" % (title, res["title"])
    return msg, 200, {'Content-Type': 'text/Plain'}

