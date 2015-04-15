import time
from dateutil import rrule
import datetime
import calendar


def get_working_days(date_start_obj, date_end_obj):
    weekdays = rrule.rrule(rrule.DAILY, byweekday=range(0, 5),
                           dtstart=date_start_obj, until=date_end_obj)
    weekdays = len(list(weekdays))
    if int(time.strftime('%H')) >= 18:
        weekdays -= 1
    return weekdays


def get_month_end_for_date(date):
    return datetime.date(year=date.year,
                         month=date.month,
                         day=calendar.monthrange(date.year, date.month)[1])


def get_current_month_end():
    now = datetime.datetime.now()
    return datetime.date(year=now.year, month=now.month,
                         day=calendar.monthrange(now.year, now.month)[1])


def get_current_month_start():
    now = datetime.datetime.now()
    return datetime.date(year=now.year, month=now.month, day=1)


def get_working_hours_this_month():
    start_of_month = get_current_month_start()
    end_of_month = get_current_month_end()
    # 8 - number of hours in a day
    return get_working_days(start_of_month, end_of_month) * 8


def get_working_hours_until_now():
    start_of_month = get_current_month_start()
    now = datetime.datetime.now()
    return get_working_days(start_of_month, now) * 8
