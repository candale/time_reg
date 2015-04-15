from django.conf.urls import include, url, patterns
from django.contrib import admin

from app.views import login_or_redirect, TimeRegistrationView
import app

api_patterns = (
)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login_or_redirect),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^', include('app.urls')),

    # API views
    url(r'^api/time_registrations/(?P<id>\d+).json$',
        TimeRegistrationView.as_view()),
    url(r'^api/time_registrations.json', TimeRegistrationView.as_view()),
    url(r'^api/statistics/', include(app.urls))
)
