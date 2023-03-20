import time


def date_2_timestamp(date: str):
    return time.mktime(time.strptime(date, '%Y-%m-%d'))


def datetime_2_timestamp(datetime: str):
    return time.mktime(time.strptime(datetime, '%Y-%m-%d %H:%M:%S'))


def timestamp_2_date(timestamp: int):
    return time.strftime('%Y-%m-%d', time.localtime(timestamp))


def timestamp_2_datetime(timestamp: int):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
