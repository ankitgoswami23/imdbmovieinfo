from flask_restful import Api
from imdbmovie import app

# Registered Flask Rest API
movie_api = Api(app)

from flask import Blueprint

# Blueprint for process_controller
imdb_movie_blueprint = Blueprint('movie_info', __name__)

# Add REST-API in Blueprint
movie_api.blueprint_setup = imdb_movie_blueprint
movie_api.blueprint = imdb_movie_blueprint

from imdbmovie.movieinfo import api_endpoints

# Registered Blueprints
app.register_blueprint(imdb_movie_blueprint)

# # Integration of Swagger API Documentation
# BASE_URL = '/v1-docs'
# API_URL = '/static/endpoints/software_management.yaml'

# if app.config.get('DEBUG'):
#     api_docs_blueprint = get_swaggerui_blueprint(
#         base_url=BASE_URL,
#         api_url=API_URL,
#         config={
#             'app_name': 'Software Management'
#         },
#         blueprint_name=software_management_blueprint
#     )
#
#     # Blueprint for API Endpoint Documentation 1.0(v1)
#     app.register_blueprint(api_docs_blueprint, url_prefix=BASE_URL)
