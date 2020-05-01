import unittest2
import datetime
from gist.date_utils import DateUtis

class TestDateConvert(unittest2.TestCase):
    def setUp(self):
        self.date_utils = DateUtis()

    def test_convert_datetime_to_string_success(self):
        try:
            date_format = '%Y/%m/%d %H:%M:%S%z'
            date_to_convert = '2016/12/07 15:19:53+00:00'
            date_converted = self.date_utils.convert_string_to_datetime(date_to_convert, date_format)
            self.assertTrue(date_converted)
        except ValueError:
            self.fail("convert_date_to_string raised ValueError unexpectedly!")

    def test_convert_datetime_to_string_error(self):
        date_format = '%Y/%m/%d %H:%M:%S%z'
        date_to_convert = '2016-12-07 15:19:53+00:00'
        with self.assertRaises(ValueError):
            date_converted = self.date_utils.convert_string_to_datetime(date_to_convert, date_format)

    def test_convert_date_to_iso_default_timezone_success(self):
        try:
            date_format = '%Y:%m:%d %H:%M:%S%z'
            date_to_convert = '2016:12:07 15:19:53+00:00'
            date_converted = self.date_utils.convert_datetime_to_iso(date_to_convert, date_format)
            self.assertEqual(date_converted, '2016-12-07T13:19:53-02:00', 'Should be 2016-12-07T13:19:53-02:00')
        except ValueError:
            self.fail("convert_date_to_iso raised ValueError unexpectedly!")


    def test_convert_date_to_iso_custom_timezone_success(self):
        try:
            date_format = '%Y:%m:%d %H:%M:%S%z'
            date_to_convert = '2016:12:07 15:19:53+00:00'
            timezone = 'America/New_York'
            date_converted = self.date_utils.convert_datetime_to_iso(date_to_convert, date_format, timezone)
            self.assertEqual(date_converted, '2016-12-07T10:19:53-05:00', 'Should be 2016-12-07T10:19:53-05:00')
        except ValueError:
            self.fail("convert_date_to_iso raised ValueError unexpectedly!")

    def test_convert_date_to_iso_timezone_error(self):
        date_format = '%Y:%m:%d %H:%M:%S%z'
        date_to_convert = '2016:12:07 15:19:53+00:00'
        timezone = 'invalid_timezone'
        with self.assertRaises(ValueError):
            date_converted = self.date_utils.convert_datetime_to_iso(date_to_convert, date_format, timezone)

if __name__ == "__main__":
    unittest.main()