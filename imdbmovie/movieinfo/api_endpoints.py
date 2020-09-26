"""
REST-API related API/routes will be listed here
"""
from imdbmovie.movieinfo import movie_api
from imdbmovie.movieinfo.resources import GetDataIMDB

# Register REST API
movie_api.add_resource(GetDataIMDB, '/')
