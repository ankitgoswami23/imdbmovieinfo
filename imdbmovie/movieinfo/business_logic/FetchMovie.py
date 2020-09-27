from imdbmovie import db
from sqlalchemy import desc
from imdbmovie.movieinfo.dbmodel.ModelMovieInfo import MovieInfo
from imdbmovie.movieinfo.business_logic.common_utilities import ObjToDict


class GetAllMovies:

    def get_movies(self, order=None, descending=False):
        """
        get all movie list either order by or not.
        :param order: contain order by field
        :param descending: true or false
        :return: all movie list either order by or not as per user request
        """
        movie_list = None
        try:
            data = self.get_movie(order=order, descending=descending)
            if data:
                movie_list = ObjToDict.object_as_dict(obj=data)
        except Exception as e:
            print(e)
        if movie_list:
            return movie_list, 200
        else:
            return movie_list, 204

    @staticmethod
    def get_movie(order=None, descending=False):
        """
        Get All Movie list from the database
        :param order: contain order by field
        :param descending: true or false
        :return: all movies object
        """
        data = None
        try:
            if order == 'movie_name':
                data = db.session.query(MovieInfo).order_by(MovieInfo.movie_name).all() if descending is False else \
                    db.session.query(MovieInfo).order_by(desc(MovieInfo.movie_name)).all()
            elif order == 'movie_rating':
                data = db.session.query(MovieInfo).order_by(MovieInfo.movie_rating).all() if descending is False else \
                    db.session.query(MovieInfo).order_by(desc(MovieInfo.movie_rating)).all()
            elif order == 'movie_release':
                data = db.session.query(MovieInfo).order_by(MovieInfo.movie_release).all() if descending is False else \
                    db.session.query(MovieInfo).order_by(desc(MovieInfo.movie_release)).all()
            elif order == 'movie_duration':
                data = db.session.query(MovieInfo).order_by(MovieInfo.movie_duration).all() if descending is False else\
                    db.session.query(MovieInfo).order_by(desc(MovieInfo.movie_duration)).all()
            else:
                data = db.session.query(MovieInfo).all()
        except Exception as e:
            print(e)
        return data


class MovieSearch:

    @staticmethod
    def search_movie(string):
        """
        Search movie by name and description
        :param string:search string
        :return: result as a list
        """
        movie_list = []
        try:
            data = db.session.query(MovieInfo).filter(MovieInfo.movie_name.contains(string) |
                                                      MovieInfo.movie_desc.contains(string)).all()
            if data:
                movie_list = ObjToDict.object_as_dict(obj=data)
        except Exception as e:
            print(e)

        if movie_list:
            return movie_list, 200
        else:
            return movie_list, 204


