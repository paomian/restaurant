from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from restaurant.menu.admin import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurant.views.home', name='home'),
    # url(r'^restaurant/', include('restaurant.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$','restaurant.menu.views.index_view'),
)
urlpatterns += patterns('',
		(r'^menu/', include('restaurant.menu.urls')),
		)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
