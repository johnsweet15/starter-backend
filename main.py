from flask import Flask
from flask_cors import CORS, cross_origin
from flask_jwt import JWT
import flask_profiler

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["flask_profiler"] = {
    "enabled": True,
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth":{
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
        "^/static/.*",
        "/testing/health"
    ]
}

CORS(app)

from APIs.LoginAPI import loginBP
from APIs.ProfileAPI import profileBP

app.register_blueprint(loginBP, url_prefix="/login")
app.register_blueprint(profileBP, url_prefix="/profile")

app.secret_key = "438u10209jd023t035g129e32rj2oplbg34"

flask_profiler.init_app(app)

if __name__ == '__main__':
    app.run()