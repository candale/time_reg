from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.serializers import TimeRegistrationSerializer
from app.models import TimeRegistration
from app.services import StatisticsService


@login_required
def index(request):
    return HttpResponseRedirect(reverse('registration'))


def login_or_redirect(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    else:
        return login(request)


@login_required
def registration(request):
    return render(request, 'registration.html', {})


@api_view(('GET',))
def header_statistics(request):
    result = StatisticsService.get_header_statistics(request.user)
    return Response(result)


class TimeRegistrationView(APIView):

    queryset = TimeRegistration.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = "id"

    def get(self, request):
        time_registrations = TimeRegistration.objects.filter(
            user__pk=request.user.id).order_by('registration_day')
        serializer = TimeRegistrationSerializer(
            time_registrations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TimeRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = request.user.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        time_registration = TimeRegistration.objects.get(
            pk=int(kwargs.get(self.lookup_url_kwarg)))

        serializer = TimeRegistrationSerializer(
            time_registration, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        time_registration = TimeRegistration.objects.get(
            pk=int(kwargs.get(self.lookup_url_kwarg)))

        time_registration.delete()
        return Response(status=status.HTTP_200_OK)
