"""
WSGI config for hexagami project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, site, sys

site.addsitedir('/home/webapps/vhexagami/lib/python3.4/site-packages')

sys.path.append('/home/webapps/vhexagami')
sys.path.append('/home/webapps/vhexagami/hexagami')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hexagami.settings")

application = get_wsgi_application()
