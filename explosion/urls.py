from django.conf.urls import url, patterns
from explosion import views

urlpatterns = patterns('',
        url(r'^$', views.landing_page),
        url(r'^rules$', views.rules),
        url(r'^contact_us/$', views.contact_us),
)

