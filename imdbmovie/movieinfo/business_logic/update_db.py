from imdbmovie import db, app, celery
from imdbmovie.movieinfo.dbmodel.ModelMovieInfo import MovieInfo
from imdbmovie.movieinfo.business_logic.common_utilities import Utilities
from bs4 import BeautifulSoup
from requests import get
from json import loads, dumps


class UpdateMovieDB:

    @staticmethod
    @celery.task
    def update_movie_db():
        """
        Update Database from IMDB Server
        :return: True or False
        """
        status = "False"
        try:
            print('start')
            db.session.query(MovieInfo).delete()
            imbd_url = app.config.get('IMDBURL')
            requested_data = get(imbd_url + "chart/top?ref_=nv_mv_250")
            soup = BeautifulSoup(requested_data.content, 'html.parser')
            for index, movie_data in enumerate(soup.findAll(attrs={"class": "titleColumn"})):
                movie_link = imbd_url + movie_data.find('a').attrs.get('href')
                movie_info = get(movie_link)
                movie_info = BeautifulSoup(movie_info.content, 'html.parser')
                movie_info = loads(movie_info.find('script', {"type": 'application/ld+json'}).string)
                data = {
                    'id': index+1,
                    'movie_name': movie_info.get('name'),
                    'movie_rating': movie_info.get('aggregateRating').get('ratingValue'),
                    'movie_release': movie_info.get('datePublished'),
                    'movie_duration': Utilities.get_duration(dur_time=movie_info.get('duration')),
                    'movie_desc': dumps({'description': movie_info.get('description')})
                }
                print(data)
                obj_scheduler_data = MovieInfo(**data)
                db.session.add(obj_scheduler_data)
                query = db.session.commit()
                if query is None:
                    status = "True"
                db.session.close()
        except Exception as e:
            print(e)

        return status, 200

@celery.task
def test_print(test):
    print(test)
    print("Test")