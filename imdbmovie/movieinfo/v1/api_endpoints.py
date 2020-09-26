"""
REST-API related API/routes will be listed here
"""
from imdbmovie.movieinfo import movie_api
from imdbmovie.movieinfo.v1.resources import TestAPI

# Register REST API
# Endpoints for API version 1.0 (api-v1)
# movie_api.add_resource(SoftwareManagement, '/software-management')
movie_api.add_resource(TestAPI, '/test-api')
