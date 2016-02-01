from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$','certificados.views.inicio'),
                       url(r'^usuarios/$','certificados.views.usuarios'),
                       url(r'^usuario/nuevo$','certificados.views.crear_usuario'),
                       url(r'^provincia/$','certificados.views.crear_provincia'),
                       url(r'^ciudad/$','certificados.views.crear_ciudad'),
                       url(r'^direccion/nueva$','certificados.views.crear_direccion'),
                       url(r'^transaccion/$','certificados.views.crear_transaccion'),
                       url(r'^get_ciudades/(?P<prov_id>\d+)/$','certificados.views.get_ciudades'),
                       url(r'^media/(?P<path>.*)$','django.views.static.serve',
                           {'document_root':settings.MEDIA_ROOT,}),
                       url(r'^admin/', include(admin.site.urls))
)