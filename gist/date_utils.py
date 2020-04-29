import datetime
import time

def convert_datetime_to_timestamp(datetime_convert, datetime_format):
    try:
        date = datetime.datetime.strptime(datetime_convert, datetime_format)
        local_time = date.astimezone().timetuple()
        return time.mktime(local_time)
    except:
        raise ValueError("Error convert datetime to timestamp") 