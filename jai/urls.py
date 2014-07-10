from django.conf.urls import patterns, include, url
from factura.views import index,wsInsertarProducto,wsBuscarFolio,autocompleteRfc,wsBuscarReceptor
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jai.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	(r'^facturar/$',index),
	(r'^ws/insertar/producto/$',wsInsertarProducto),
	(r'^ws/buscar/folio/$',wsBuscarFolio),
	(r'^ws/search/json/$',autocompleteRfc),
	(r'^ws/buscar/receptor/$',wsBuscarReceptor),
	
    url(r'^admin/', include(admin.site.urls)),
)
