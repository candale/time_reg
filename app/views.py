from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'registration.html', {})


def login_or_redirect(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    else:
        return login(request)
