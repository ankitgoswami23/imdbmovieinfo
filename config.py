from os.path import dirname, abspath

from imdbmovie.utilities.settings.site_config import SiteConfig

site_config = SiteConfig(config_file='development.yaml').get_config()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))

# JWT Authentication Configuration
SECRET_KEY = site_config.get('secrets', {}).get('SECRET_KEY', '')
JWT_CONFIG = site_config.get('jwt_config', {})
PROPAGATE_EXCEPTIONS = site_config.get('exception', {}).get('PROPAGATE_EXCEPTIONS', True)

# imdb url
IMDBURL = site_config.get('imdb_url', {}).get('IMDB_URL', 'https://www.imdb.com/')

DEBUG = site_config.get('debug', {}).get('DEBUG', False)

SERVICE_HOST = site_config.get('running_host', {}).get('host', '0.0.0.0')
SERVICE_PORT = site_config.get('running_host', {}).get('port', 8080)

# Database configurations
DATABASE = site_config.get('database', {}).get('NAME', '')
ENGINE = site_config.get('database', {}).get('ENGINE', '')
USERNAME = site_config.get('database', {}).get('USER', '')
PASSWORD = site_config.get('database', {}).get('PASSWORD', '')
HOST = site_config.get('database', {}).get('HOST', '0.0.0.0')
PORT = site_config.get('database', {}).get('PORT', 3306)

# SQLAlchemy Configurations
SQLALCHEMY_DATABASE_URI = f'{ENGINE}://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = site_config.get('database', {}).get('SQLALCHEMY_TRACK_MODIFICATIONS', False)

# Application definition
INSTALLED_APPS = site_config.get('installed_apps', [])

THIS_URL = str(SERVICE_HOST) + ":" + str(SERVICE_PORT)