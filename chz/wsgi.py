"""
WSGI config for chz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import sys

sys.path.append('/var/www/chz')
# sys.path.append('/usr/local/python/lib/python2.7/site-packages')
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chz.settings")

application = get_wsgi_application()
