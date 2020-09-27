from imdbmovie import db, app
from imdbmovie.movieinfo.dbmodel.ModelMovieInfo import MovieInfo
from imdbmovie.movieinfo.business_logic.common_utilities import ObjToDict


class GetAllMovies:
    def __init__(self):
        pass

    def get_movies(self, order=None):
        movie_list = None
        try:
            if order == 'movie_name':
                data = db.session.query(MovieInfo).order_by(MovieInfo.movie_name).all()
            elif order == 'movie_rating':
                data = db.session.query(MovieInfo).order_by(MovieInfo.movie_name).all()
            elif order == 'movie_release':
                data = db.session.query(MovieInfo).order_by(MovieInfo.movie_release).all()
            elif order == 'movie_duration':
                data = db.session.query(MovieInfo).order_by(MovieInfo.movie_duration).all()
            else:
                data = db.session.query(MovieInfo).all()
            if data:
                movie_list = ObjToDict.object_as_dict(obj=data)
        except Exception as e:
            print(e)
        return movie_list


class MovieSearch:

    def __init__(self):
        pass

    @staticmethod
    def search_movie(string):
        movie_list = []
        try:
            data = db.session.query(MovieInfo).filter(MovieInfo.movie_name.contains(string) |
                                                      MovieInfo.movie_desc.contains(string)).all()
            if data:
                movie_list = ObjToDict.object_as_dict(obj=data)
        except Exception as e:
            print(e)
        return movie_list


