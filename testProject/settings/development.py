import os
from testProject.settings.base import *
from django.core.management.utils import get_random_secret_key
ALLOWED_HOSTS = ['127.0.0.1','localhost']

DEBUG = True

SECRET_KEY = get_random_secret_key()

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

