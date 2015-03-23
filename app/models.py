from django.contrib.auth.models import User
from django.db import models


class TimeRegistration(models.Model):

    SOURCE_CHOICES = [
        ('M', "Manual"),
        ('A', "Auto"),
    ]

    user = models.ForeignKey(User, related_name='time_registrations')

    project = models.CharField(max_length=50, null=False, blank=False)
    task_code = models.CharField(max_length=50, null=False, blank=False)
    registration_day = models.DateField(null=False, blank=False)
    time = models.BigIntegerField(null=False, blank=False)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES,
                              null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "User: {} Task: {}".format(self.user.username, self.task_code)

    def get_time_str(self):
        hours = self.time / 60
        minutes = round((self.time / 60.0) - hours, 1)

        if not minutes:
            total_time = str(hours)
        else:
            total_time = str(hours + minutes)

        return total_time

    @classmethod
    def get_normalized_time_from_string(cls, time_str):
        '''
        time_str must be the string representation of a float value
        it may be trailed by a 'h' (e.g. 3.5h)
        '''
        striped_value = time_str.strip()
        if striped_value.find('h') >= 0:
            if striped_value.find('h') != len(striped_value) - 1:
                raise ValueError('Invalid time string')
            striped_value = striped_value[:len(striped_value) - 1]

        float_value = float(striped_value)

        if float_value <= 0:
            raise ValueError('Time cannot be zero or negative')

        return float_value

    @classmethod
    def get_time_from_str(cls, str_time):
        normalized_time = cls.get_normalized_time_from_string(str_time)
        return int(normalized_time * 60)
