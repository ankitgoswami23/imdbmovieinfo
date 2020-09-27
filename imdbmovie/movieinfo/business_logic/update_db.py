from imdbmovie import db, app
from imdbmovie.movieinfo.dbmodel.ModelMovieInfo import MovieInfo
from bs4 import BeautifulSoup
from requests import get
from json import loads, dumps


class UpdateMovieDB:

    def update_movie_db(self):
        """
        Update Database from IMDB Server
        :return: True or False
        """
        status = "False"
        try:
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
                    'movie_duration': self.get_duration(dur_time=movie_info.get('duration')),
                    'movie_desc': dumps({'description': movie_info.get('description')})
                }
                obj_scheduler_data = MovieInfo(**data)
                db.session.add(obj_scheduler_data)
            query = db.session.commit()
            if query is None:
                status = "True"
            db.session.close()
        except Exception as e:
            print(e)

        return status, 200

    @staticmethod
    def get_duration(dur_time):
        """
        Parse Duration Time from the server and return minutes
        :param dur_time: Duration String which get from server
        :return: minutes
        """
        duration = [0]
        try:
            duration = dur_time.replace('PT', '').replace('M', '').split('H')
            if len(duration) > 1:
                hour = 0 if duration[0] in ['', None] else int(duration[0])
                minute = 0 if duration[1] in ['', None] else int(duration[1])
                duration = (hour * 60) + minute
            elif 'M' in dur_time and 'H' not in dur_time:
                duration = duration[0]
            elif 'H' in dur_time and 'M' not in dur_time:
                duration = duration[0] * 60
        except Exception as e:
            print(e)
        return duration
