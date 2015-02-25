from rest_framework import serializers

from app.models import TimeRegistration


class TimeRegistrationSerializer(serializers.ModelSerializer):

    registration_day = serializers.DateField(format="%d/%m/%Y",
                                             input_formats=["%d/%m/%Y"])
    source = serializers.ChoiceField(choices=TimeRegistration.SOURCE_CHOICES)
    time_str = serializers.CharField(source="get_time_str")

    class Meta:
        model = TimeRegistration
        lookup_field = 'id'

        fields = ('project', 'task_code', 'registration_day',
                  'time_str', 'source', 'id')

    def validate_time_str(self, value):
        striped_value = value.strip()
        if striped_value.find('h') >= 0:
            if striped_value.find('h') != len(striped_value) - 1:
                raise serializers.ValidationError('Invalid time string')
            striped_value = striped_value[:len(striped_value) - 1]

        try:
            float_value = float(striped_value)
        except ValueError:
            raise serializers.ValidationError('Invalid time string')

        if float_value <= 0:
            raise serializers.ValidationError(
                'Time cannot be zero or negative')

        return value

    def save(self, *args, **kwargs):
        self.instance.set_time_from_str(self.validated_data['get_time_str'])
        time_str = self.instance.get_time_str()
        # this is weird behaviour, the method get_time_str is replaces with
        # the validated data for time_str
        super(TimeRegistrationSerializer, self).save(*args, **kwargs)
        self.data['time_str'] = time_str
