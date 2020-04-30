import unittest2
import datetime
from gist.date_utils import DateUtis

class TestDateConvert(unittest2.TestCase):
    def setUp(self):
        self.date_utils = DateUtis()

    def test_convert_date_success(self):
        try:
            date_format = '%Y:%m:%d %H:%M:%S'
            date_converted = self.date_utils.convert_datetime_to_timestamp('2019:01:31 09:15:28', date_format)
            self.assertEqual(date_converted, 1548933328.0, 'Should be 1548933328.0')
        except ValueError:
            self.fail("convert_datetime_to_timestamp raised ValueError unexpectedly!")

    def test_convert_date_error(self):
        date_format = '%Y:%m:%d %H:%M:%S'
        date_to_convert = 'invalid_date'
        with self.assertRaises(ValueError):
            date_converted = self.date_utils.convert_datetime_to_timestamp(date_to_convert, date_format)

if __name__ == "__main__":
    unittest.main()