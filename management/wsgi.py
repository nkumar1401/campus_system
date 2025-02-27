import os

from django.core.wsgi  import get_wsgi_application 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')  # Ensure 'management' is correct

application = get_wsgi_application()
