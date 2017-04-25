from __future__ import absolute_import, unicode_literals

import os

from .base import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['infinite-crag-79176.herokuapp.com']

# force https
SECURE_SSL_REDIRECT = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')



try:
    from .local import *
except ImportError:
    pass
