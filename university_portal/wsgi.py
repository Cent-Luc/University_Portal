"""
WSGI config for university_portal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from pathlib import Path
from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv
ENV_PATH = Path('..') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_portal.settings')

application = get_wsgi_application()
