from flask_restful import Resource
from flask import request, jsonify
from imdbmovie.movieinfo.business_logic.update_db import UpdateMovieDB
from imdbmovie.movieinfo.business_logic.FetchMovie import GetAllMovies, MovieSearch


class UpdateMovieInDb(Resource):

    def __init__(self):
        pass

    @staticmethod
    def get():
        return UpdateMovieDB().update_movie_db()


class GetMovieList(Resource):
    def __init__(self):
        pass

    @staticmethod
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
    def get():
        response = None
        data = request.args.get('string', None)
        if data:
            response = MovieSearch().search_movie(data)

        if response:
            return response, 200
        else:
            return response, 204

