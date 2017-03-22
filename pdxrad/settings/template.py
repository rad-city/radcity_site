from .base import *

SITE_ID=1

DEBUG = True

ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT = False

#BE SURE TO CHANGE THIS
SECRET_KEY='1(y%e_42=&ikz&h622g1_jjd7rv!uu!m55$2ma4-+ca+rok961'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

#Email Options
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'mail.example.com'
EMAIL_HOST_USER = 'admin@example.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'admin@example.com'

#Media
MEDIA_ROOT = '/home/user/media/'
MEDIA_URL = '/media/'


STATIC_URL = '/static/'
CKEDITOR_UPLOAD_PATH = "uploads/"

#Storage Settings
DEFAULT_FILE_STORAGE = 'storages.backends.gs.GSBotoStorage'
GS_ACCESS_KEY_ID = 'YourID'
GS_SECRET_ACCESS_KEY = 'YourKEY'
GS_BUCKET_NAME = 'YourBucket'
STATICFILES_STORAGE = 'storages.backends.gs.GSBotoStorage'
