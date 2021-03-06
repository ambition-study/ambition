from ...sites import get_site_id
from .base_live import *

# for django.contrib.sites
SITE_ID = get_site_id('blantyre')

WSGI_APPLICATION = 'ambition.wsgi.blantyre.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'blantyre.ambition.bhp.org.bw']

TIME_ZONE = 'Africa/Blantyre'
