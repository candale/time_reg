from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url('^$', views.index, name='index'),
    url('^registration/', views.registration, name='registration'),
    url('^header-statistics.json', views.header_statistics,
        name='header_statistics')
)
