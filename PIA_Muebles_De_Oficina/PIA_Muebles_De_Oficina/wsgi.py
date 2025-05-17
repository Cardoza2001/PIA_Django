"""
WSGI config for PIA_Muebles_De_Oficina project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PIA_Muebles_De_Oficina.settings')

application = get_wsgi_application()
