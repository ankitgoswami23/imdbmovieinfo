from flask_restful import Resource
from flask import request
from imdbmovie.movieinfo.business_logic.update_db import UpdateMovieDB
from imdbmovie.movieinfo.business_logic.FetchMovie import GetAllMovies, MovieSearch


class UpdateMovieInDb(Resource):

    def __init__(self):
        pass

    def get(self):
        return UpdateMovieDB().update_movie_db()


class GetMovieList(Resource):
    def __init__(self):
        pass

    def get(self):
        return GetAllMovies().get_movies()


class SearchMovie(Resource):
    def __init__(self):
        pass

    def get(self):
        data = request.args.get('string')
        return MovieSearch().search_movie(data)