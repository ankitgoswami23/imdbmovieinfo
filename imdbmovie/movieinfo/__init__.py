from flask_restful import Api
from imdbmovie import app

# Registered Flask Rest API
movie_api = Api(app)

from flask import Blueprint

# Blueprint for Movie Info
imdb_movie_blueprint = Blueprint('movie_info', __name__)

# Add REST-API in Blueprint
movie_api.blueprint_setup = imdb_movie_blueprint
movie_api.blueprint = imdb_movie_blueprint

from imdbmovie.movieinfo import api_endpoints

# Registered Blueprints
app.register_blueprint(imdb_movie_blueprint)