
from datetime import datetime as dt
import calendar

class MyDateTime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            now = dt.utcnow()
            self._datetime = dt(now.year, now.month, now.day, hour, minute, second)
        else:
            self._validate_date(year, month, day)
            self._datetime = dt(year, month, day, hour, minute, second)

    @classmethod
    def from_iso_format(cls, iso_string):
        pass

    @staticmethod
    def _validate_date(year, month, day):
        pass

    def iso_format(self):
        return self._datetime.isoformat()

    def human_readable_format(self):
        return self._datetime.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def format_helper(date, time_format):
        pass

    @staticmethod
    def convert_between_calendars(date, from_calendar, to_calendar):
        pass

    @staticmethod
    def weekday_calculation(date):
        pass

    @classmethod
    def date_difference(cls, date1, date2):
        pass


import pytest

def test_default_datetime_creation():
    my_datetime = MyDateTime()
    assert isinstance(my_datetime, MyDateTime)

def test_iso_format():
    my_datetime = MyDateTime(2023, 1, 1, 12, 30, 45)
    assert my_datetime.iso_format() == '2023-01-01T12:30:45'

