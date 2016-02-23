from django.conf.urls import patterns, include, url
from commitinfo import views
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin 
#admin.autodiscover()
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls),name='xadmin'),
    url(r'^$', views.index, name='index'),
    url(r'^kernel$', views.index,name='kernel'),
    url(r'^libvirt$', views.libvirt_page,name='libvirt'),
    url(r'^openstack$', views.openstack_page,name='openstack'),
)
