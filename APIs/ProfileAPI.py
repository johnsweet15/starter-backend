from flask import Flask, Blueprint, request
from pymongo import MongoClient
from passlib.hash import sha256_crypt

from Models.Profile import Profile

from Utils.ConfigParser import config

import json
import uuid


profileBP = Blueprint("profile", __name__)

@profileBP.route('/createProfile', methods=['POST'])
def createProfile():
    username = request.json.get('username')
    password = request.json.get('password')

    profile = Profile()

    profileId = str(uuid.uuid4())

    profile.setProfileId(profileId)
    profile.setUsername(username)
    profile.setPassword(sha256_crypt.encrypt(password))

    client = MongoClient(config['mongoDB']['url'])
    db = client.Flaskredux
    collection = db['profile']

    collection.insert_one(profile.__dict__)

    client.close()

    return {'success': False}