"""
WSGI config for WebMinePlus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebMinePlus.settings')

application = get_wsgi_application()


# ----------------------------------
#             Chuly
#     GitHub: https://github.com/victoryanezn
#     Discord: chuly2005#0
# ---------------------------------- 