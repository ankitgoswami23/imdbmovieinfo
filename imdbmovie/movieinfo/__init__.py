from flask_restful import Api
from imdbmovie import app

# Registered Flask Rest API
movie_api = Api(app)

from imdbmovie.movieinfo import api_endpoints
