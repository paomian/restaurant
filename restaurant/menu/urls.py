from django.conf.urls.defaults import *
from models import *
from views import *
from resource import *

urlpatterns = patterns('',
		(r'create/$',create_dish),
        (r'list/$',list_dish),
        (r'edit/edit/(?P<id>[^/]+)/$',edit_dish),
        (r'accounts/login/$',login_view),
        (r'accounts/logout/$',logout_view),
		)
