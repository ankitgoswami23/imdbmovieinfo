from flask import request
from flask_restful import Resource
from requests import get
from bs4 import BeautifulSoup
from json import loads


class GetDataIMDB(Resource):
    def __init__(self):
        pass

    def get(self):
        try:
            movie_rating = 0
            print('start')
            imbd_url = "https://www.imdb.com/"
            requested_data = get(imbd_url + "chart/top?ref_=nv_mv_250")
            soup = BeautifulSoup(requested_data.content, 'html.parser')
            for index, movie_data in enumerate(soup.findAll(attrs={"class": "titleColumn"})):
                print('start for ', index+1, ':', '\n', )
                movie_link = imbd_url + movie_data.find('a').attrs.get('href')
                movie_info = get(movie_link)
                movie_info = BeautifulSoup(movie_info.content, 'html.parser')
                movie_info = loads(movie_info.find('script', {"type": 'application/ld+json'}).string)
                movie_name = movie_info.get('name')
                movie_duration = movie_info.get('duration')
                movie_release = movie_info.get('datePublished')
                movie_rating = movie_info.get('aggregateRating').get('ratingValue')
                movie_desc = movie_info.get('description')
                print(movie_name, '\n', movie_duration, '\n', movie_release, '\n', movie_rating, '\n', movie_desc)
                print('-----------------------------------------------------------------------------------------')

        except Exception as e:
            print(e)
        return "requested_data"