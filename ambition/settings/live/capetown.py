from ...sites import get_site_id
from .base_test import *

# for django.contrib.sites
SITE_ID = get_site_id('capetown')

WSGI_APPLICATION = 'ambition.wsgi.capetown.application'
