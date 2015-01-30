from django.contrib.auth.models import User
from django.db import models


class TimeRegistration(models.Model):

    SOURCE_CHOICES = [
        (0, "Manual"),
        (1, "Auto"),
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
