from scheduler import Scheduler
from professor import Professor
from course import Course
from final import Final
from session import Session
import datetime
import unittest


class TestScheduler(unittest.TestCase):

    def test_scheduler_empty_course_list(self):
        courses = []
        max_units = 20
        course_numbers = {'100', '200', '300'}
        min_days_between_finals = 1
        self.assertEqual(Scheduler.get_schdeules(
            courses, max_units, course_numbers, min_days_between_finals), [])

    def test_get_courses_by_numbers_empty_course_list(self):
        courses = []
        course_numbers = {'100', '200'}
        self.assertEqual(Scheduler.get_courses_by_numbers(
            courses, course_numbers), [])

    def test_get_courses_by_numbers_empty_course_number_set(self):
        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [], None)
        course_2 = Course(1, '321', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [], None)
        courses = []
        course_numbers = set()
        self.assertEqual(Scheduler.get_courses_by_numbers(
            courses, course_numbers), [])


if __name__ == '__main__':
    unittest.main()
