"""
WSGI config for personal_website2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

# for production
sys.path.append("/var/www/html/personal_website2")
sys.path.append("var/www/html/personal_website2/personal_website2")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_website2.settings')

application = get_wsgi_application()
