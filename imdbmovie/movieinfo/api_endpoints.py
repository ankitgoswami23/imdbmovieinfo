"""
REST-API related API/routes will be listed here
"""
from imdbmovie.movieinfo import movie_api
from imdbmovie.movieinfo.resources import UpdateMovieInDb, GetMovieList, SearchMovie

# Register REST API
movie_api.add_resource(UpdateMovieInDb, '/update_movie_db')
movie_api.add_resource(GetMovieList, '/get_movie')
movie_api.add_resource(SearchMovie, '/get_movie/search')
