import datetime
import time
import pytz

class DateUtis:
    @staticmethod
    def convert_string_to_datetime(datetime_convert, datetime_format):
        try:
            return datetime.datetime.strptime(datetime_convert, datetime_format)
        except:
            raise ValueError("Error convert datetime to string")

    @staticmethod
    def convert_datetime_to_iso(datetime_convert, datetime_format, timezone_convert='America/Sao_Paulo'):
        try:
            timestamp = DateUtis.convert_string_to_datetime(datetime_convert, datetime_format)
            tz = pytz.timezone(timezone_convert)
            return timestamp.astimezone(tz=tz).isoformat() 
        except:
            raise ValueError("Error convert datetime to iso format")