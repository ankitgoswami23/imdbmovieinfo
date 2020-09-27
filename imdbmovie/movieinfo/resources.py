from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from imdbmovie.movieinfo.business_logic.update_db import UpdateMovieDB
from imdbmovie.movieinfo.business_logic.FetchMovie import GetAllMovies, MovieSearch
from imdbmovie.movieinfo.business_logic.common_utilities import Authoraization


class GetAuthToken(Resource):
    def __init__(self):
        pass

    def post(self):
        data = request.get_json(force=True)
        return Authoraization().validate_credentials(data=data)


class UpdateMovieInDb(Resource):

    def __init__(self):
        pass

    @staticmethod
    @jwt_required
    def get():
        return UpdateMovieDB().update_movie_db()


class GetMovieList(Resource):
    def __init__(self):
        pass

    @staticmethod
    @jwt_required
    def get():
        response = None
        try:
            sort_by = request.args.get('sort_by', None)
            response = GetAllMovies().get_movies(order=sort_by)
            return response, 200
        except Exception as e:
            print(e)
            return response, 204


class SearchMovie(Resource):
    def __init__(self):
        pass

    @staticmethod
    @jwt_required
    def get():
        response = None
        data = request.args.get('string', None)
        if data:
            response = MovieSearch().search_movie(data)

        if response:
            return response, 200
        else:
            return response, 204

