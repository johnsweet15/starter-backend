from flask import Flask, Blueprint, request, session
from pymongo import MongoClient
from passlib.hash import sha256_crypt

from Utils.ConfigParser import config

import json
import uuid

loginBP = Blueprint("login", __name__)

@loginBP.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    client = MongoClient(config['mongoDB']['url'])
    db = client.Flaskredux
    collection = db['profile']

    result = collection.find_one({'username': username})

    client.close()

    if(result != None):
        isValid = sha256_crypt.verify(password, result['password'])
        if(isValid):
            return '', 200
        else:
            return {'error': 'Incorrect username or password'}, 401
    else:
        return {'success': False, 'error': 'Username does not exist'}, 401
