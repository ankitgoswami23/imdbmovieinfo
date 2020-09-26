# File Name: app.py
# Author: Ankit Goswami
# Creation Date[DD/MM/YY]: 02/04/2020

from imdbmovie import app

if __name__ == '__main__':
    app.run(
        host=app.config.get('SERVICE_HOST'),
        port=app.config.get('SERVICE_PORT'),
        threaded=app.config.get('THREADED')
    )
