# imdbmovieinfo
IMDB Movie info Rest API Flask

Install requirements.txt
````
pip install -r requirements.txt
````
Setup Database configuration in development.yaml file

run db query from imdbmovie.sql into mysql

run project with
````
python app.py
````
##API Info

- All API Call after authentication
- Auth token send as a Bearer Token

###Update Database from IMDB Server:
- /update_movie_db - (get request)
    - Update database from IMDB Server
###Update Database from IMDB Server:
- /get_movie
    - to get all Movie info
    - request type : GET
- /get_movie?sort_by=movie_name
    - to get all Movie info with ordered by
    - request type : GET
- /get_movie?sort_by=movie_name&desc=true
    - to get all Movie info with ordered by in descending order
    - request type : GET
- /get_movie/search?string=terminator
    - search movie with description and name and return the list
    - request type : GET
- /auth/token
    - to retrieve a auth token for access all above API
    - request type : POST
    - JSON to be send 
    ``{
    "credentials": {
        "password": "pass@word",
        "username": "user@name"
    }
}``
     
Thank you
