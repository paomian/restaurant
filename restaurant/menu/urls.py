from django.conf.urls.defaults import *
from models import *
from views import *
from resource import *

urlpatterns = patterns('',
		(r'create/$',create_dish),
		)
