from os.path import dirname, abspath

from imdbmovie.utilities.settings.site_config import SiteConfig

site_config = SiteConfig(config_file='development.yaml').get_config()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = site_config.get('secrets', {}).get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = site_config.get('debug', {}).get('DEBUG', False)

SERVICE_HOST = site_config.get('running_host', {}).get('host', '0.0.0.0')
SERVICE_PORT = site_config.get('running_host', {}).get('port', 3012)
THREADED = site_config.get('running_host', {}).get('threaded', False)

ALLOWED_HOSTS = site_config.get('hosts', {}).get('ALLOWED_HOSTS', [])

# Application definition
INSTALLED_APPS = site_config.get('installed_apps', [])

THIS_URL = str(SERVICE_HOST) + ":" + str(SERVICE_PORT)