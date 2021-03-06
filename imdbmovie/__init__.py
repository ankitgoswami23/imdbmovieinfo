import importlib
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# App Initialization
app = Flask(__name__)
app.config.from_object('config')

# Initializing REST API Object
api = Api(app)

db = SQLAlchemy(app, session_options={})

jwt = JWTManager(app)

# Initializing installed app
for installed_app in app.config.get('INSTALLED_APPS', []):
    try:
        importlib.__import__(installed_app)
    except ModuleNotFoundError as e:
        print(e)
