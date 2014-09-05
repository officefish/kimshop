# -*- coding: utf-8 -*-
#!/virtualenvs/oscar/bin/python

import os, sys, site

my_virtualenv_path = "/virtualenvs/oscar/lib/python2.7/site-packages"
# Add it to your PYTHONPATH

sys.path.insert(0, my_virtualenv_path)
site.addsitedir(my_virtualenv_path)

root = os.path.join(os.path.dirname(__file__), '..')

sys.path.insert(0, '/www/django')
sys.path.insert(0, '/www/django/kimshop')
sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kimshop.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
