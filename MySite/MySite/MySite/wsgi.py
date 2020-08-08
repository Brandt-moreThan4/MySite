"""
WSGI config for MySite project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

For more information, visit
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'MySite.settings')

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()




# Below is for use on pythonanywhere

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
#import os
#import sys
#
## assuming your django settings file is at '/home/153144green/mysite/mysite/settings.py'
## and your manage.py is is at '/home/153144green/mysite/manage.py'
#path = '/home/153144green/MySite/MySite'

#if path not in sys.path:
#    sys.path.append(path)

#os.environ['DJANGO_SETTINGS_MODULE'] = 'MySite.settings'


#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
