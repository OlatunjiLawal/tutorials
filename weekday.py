import datetime
import unittest
from unittest.mock import Mock

datetime = Mock()

def get_weekday():
    date = datetime.datetime.now()
    return date.strftime("%A")

class TestGetWeekday(unittest.TestCase):
    def test_weekday(self):

        datetime.now.return_value = datetime.datetime(2024, 8, 22)
        datetime.strftime = datetime.datetime.strftime

        day_of_week = get_weekday()

        self.assertEqual(day_of_week, "Thursday")

if __name__ == '__main__':
    unittest.main()