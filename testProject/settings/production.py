import os
from testProject.settings.base import *
from django.core.management.utils import get_random_secret_key

ALLOWED_HOSTS = ['tuna-production-practice.pje89ijymw.ap-northeast-2.elasticbeanstalk.com']

DEBUG = False

SECRET_KEY = get_random_secret_key()

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')