from imdbmovie import db
from json import dumps


class MovieInfo(db.Model):
    __tablename__ = "movie_info"

    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    movie_name = db.Column('movie_name', db.String, nullable=False)
    movie_rating = db.Column('movie_rating', db.DECIMAL, nullable=False)
    movie_release = db.Column('movie_release', db.DATE, nullable=False)
    movie_duration = db.Column('movie_duration', db.Integer)
    movie_desc = db.Column('movie_desc', db.JSON)

    def __init__(self, id, movie_name, movie_rating, movie_release, movie_duration, movie_desc):
        self.id = id
        self.movie_name = movie_name
        self.movie_rating = movie_rating
        self.movie_release = movie_release
        self.movie_duration = movie_duration
        self.movie_desc = movie_desc

    # def __repr__(self):
    #     data = {'id': self.id,
    #             'movie_name': self.movie_name,
    #             'movie_rating': self.movie_rating,
    #             'movie_release': self.movie_release,
    #             'movie_duration': self.movie_duration,
    #             'movie_desc': self.movie_desc
    #             }
    #     data = dumps(data)
    #
    #     return data
