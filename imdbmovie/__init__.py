import importlib
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# App Initialization
app = Flask(__name__)
app.config.from_object('config')

# Initializing REST API Object
api = Api(app)

db = SQLAlchemy(app, session_options={})

# It's for cross platform communication
CORS(app, resources={r"/" + app.config['THIS_URL']: {"origins": "*"}})

for installed_app in app.config.get('INSTALLED_APPS', []):
    try:
        importlib.__import__(installed_app)
    except ModuleNotFoundError as e:
        print(e)
