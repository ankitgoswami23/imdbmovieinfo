from imdbmovie import app

if __name__ == '__main__':
    app.run(
        host=app.config.get('SERVICE_HOST'),
        port=app.config.get('SERVICE_PORT')
    )
