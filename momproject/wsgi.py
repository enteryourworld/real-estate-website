import os, sys
activate_this = '/home/a1038562/python/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/a1038562/domains/a1038562.xsph.ru/momproject'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'momproject.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()