from flask import Blueprint
# from flask_swagger_ui import get_swaggerui_blueprint
from imdbmovie.movieinfo import app, movie_api

# Blueprint for process_controller
software_management_blueprint = Blueprint('software_management', __name__)

# Add REST-API in Blueprint
movie_api.blueprint_setup = software_management_blueprint
movie_api.blueprint = software_management_blueprint

from imdbmovie.movieinfo.v1 import api_endpoints
from imdbmovie.movieinfo.v1 import api_endpoints

# Registered Blueprints
app.register_blueprint(software_management_blueprint)

# Integration of Swagger API Documentation
BASE_URL = '/v1-docs'
API_URL = '/static/endpoints/software_management.yaml'

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
