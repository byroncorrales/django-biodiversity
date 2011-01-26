from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import settings
from os import path as os_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^biodiversity/', include('biodiversity.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^eventos/', include('eventos.urls')),
    (r'^noticias/', include('noticias.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(.*)$', 'django.views.static.serve',
                             {'document_root': os_path.join(settings.MEDIA_ROOT)}),
                           )
