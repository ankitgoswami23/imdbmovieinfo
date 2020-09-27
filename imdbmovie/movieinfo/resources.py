from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from imdbmovie.movieinfo.business_logic.update_db import UpdateMovieDB
from imdbmovie.movieinfo.business_logic.FetchMovie import GetAllMovies, MovieSearch
from imdbmovie.movieinfo.business_logic.common_utilities import Authorization


class GetAuthToken(Resource):

    @staticmethod
    def post():
        """
        Retrieve auth token while user request
        :return: auth token
        """
        return Authorization().validate_credentials(data=request.get_json(force=True))


class UpdateMovieInDb(Resource):

    @staticmethod
    @jwt_required
    def get():
        """
        Request to update the database from the server
        :return: true or false
        """
        return UpdateMovieDB().update_movie_db()


class GetMovieList(Resource):

    @staticmethod
    @jwt_required
    def get():
        """
        Get all Movie list with sorted by or not
        :return: Movie List
        """
        return GetAllMovies().get_movies(order=request.args.get('sort_by', None),
                                         descending=request.args.get('desc', False))


class SearchMovie(Resource):

    @staticmethod
    @jwt_required
    def get():
        """
        Search Movie from the db
        :return: Movie List
        """
        return MovieSearch().search_movie(request.args.get('string', None))
