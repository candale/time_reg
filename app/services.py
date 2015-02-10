from app.models import TimeRegistration
from django.core.serializers import serialize


class RegistrationService(object):

    @classmethod
    def get_all_json_for_user(self, user):
        return serialize(
            'json',
            TimeRegistration.objects.filter(user__pk=user.id).all())
