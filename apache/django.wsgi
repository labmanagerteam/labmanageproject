import os
import sys

path = '/home/eelab/labmanageproject'
if path not in sys.path:
    sys.path.insert(0, '/home/eelab/labmanageproject')
os.environ['DJANGO_SETTINGS_MODULE'] = 'labmanageproject.settings'
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()