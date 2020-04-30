import datetime
import time

class DateUtis:
    @staticmethod
    def convert_datetime_to_timestamp(datetime_convert, datetime_format):
        try:
            date = datetime.datetime.strptime(datetime_convert, datetime_format)
            local_time = date.timetuple()
            return time.mktime(local_time)
        except:
            raise ValueError("Error convert datetime to timestamp") 