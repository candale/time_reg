import datetime

from django.core.serializers import serialize
from django.db.models import Sum

from app.models import TimeRegistration
from helpers import (
    get_working_hours_this_month, get_current_month_start,
    get_working_hours_until_now)


class RegistrationService(object):

    @classmethod
    def get_all_json_for_user(self, user):
        return serialize(
            'json', TimeRegistration.objects.filter(user__pk=user.id).all())


class StatisticsService(object):

    @classmethod
    def get_header_statistics(cls, user):
        working_hours_this_month = get_working_hours_this_month()
        working_hours_until_now = get_working_hours_until_now()

        now = datetime.datetime.now()
        month_start = get_current_month_start()
        worked_minutes = TimeRegistration.objects.filter(
            registration_day__gte=month_start,
            registration_day__lte=now,
            user=user).aggregate(Sum('time'))
        worked_minutes = worked_minutes['time__sum']

        worked_hours_this_month = round(worked_minutes / 60.0, 2)
        minutes_offset = worked_minutes - (working_hours_until_now * 60)
        remaining_hours = working_hours_this_month - worked_hours_this_month
        hours_offset = round(minutes_offset / 60.0, 2)
        return {
            'workingHoursThisMonth': working_hours_this_month,
            'workedHoursThisMonth': worked_hours_this_month,
            'hoursOffset': hours_offset,
            'remainingHours': remaining_hours,
            'importedFromJira': 0
        }
