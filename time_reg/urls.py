from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('app.urls'), name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^$', include('app.urls')),
)
