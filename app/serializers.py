from rest_framework import serializers

from app.models import TimeRegistration


class TimeRegistrationSerializer(serializers.ModelSerializer):

    registration_day = serializers.DateField(format="%d/%m/%Y",
                                             input_formats=["%d/%m/%Y"])
    source = serializers.ChoiceField(choices=TimeRegistration.SOURCE_CHOICES)

    class Meta:
        model = TimeRegistration
        lookup_field = 'id'

        fields = ('project', 'task_code', 'registration_day',
                  'time', 'source', 'id')
