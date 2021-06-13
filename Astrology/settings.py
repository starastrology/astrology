from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'mo-vaughn-is-a-special-soul-2349820934820394820394'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'need_this.apps.NeedThisConfig'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'astrology',
       }
   }
ROOT_URLCONF = 'Astrology.urls'
WSGI_APPLICATION = 'Astrology.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
#STATIC_ROOT = 'C:\\Users\\15134\\Astrology\\Django\\Astrology\\static'
STATICFILES_DIRS = ("C:\\Users\\15134\\Astrology\\Django\\Astrology\\static",)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'