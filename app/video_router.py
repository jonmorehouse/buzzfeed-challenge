from flask import request, jsonify, url_for, redirect

from app import app
from action_handler import action_handler

@app.route('/video/guess', methods=['POST'])
def create():
    res = action_handler("", request.form)


    pass

    # should return 201
    #return jsonify(action_handler("signup", request.form)), 201



     
     
     
