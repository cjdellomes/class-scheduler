from scheduler import Scheduler
from professor import Professor
from course import Course
from final import Final
from session import Session
import datetime
import unittest


class TestScheduler(unittest.TestCase):

    def test_empty_course_list(self):
        courses = []
        max_units = 20
        course_numbers = {'100', '200', '300'}
        min_days_between_finals = 1
        self.assertEqual(Scheduler.get_schdeules(
            courses, max_units, course_numbers, min_days_between_finals), [])


if __name__ == '__main__':
    unittest.main()
