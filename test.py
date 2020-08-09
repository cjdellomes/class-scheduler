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
        self.assertCountEqual(Scheduler.get_courses_by_numbers(
            courses, course_numbers), [])

    def test_get_courses_by_numbers_empty_course_number_set(self):
        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [], None)
        course_2 = Course(2, '321', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [], None)

        courses = [course_1, course_2]
        course_numbers = set()

        self.assertCountEqual(Scheduler.get_courses_by_numbers(
            courses, course_numbers), [])

    def test_get_courses_by_numbers_single_couse_number(self):
        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [], None)
        course_2 = Course(2, '321', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [], None)
        course_3 = Course(3, '121', 'course 3', None, 4, [], None)
        course_4 = Course(4, '323', 'course 4', None, 4, [], None)

        courses = [course_1, course_2, course_3, course_4]
        course_numbers = {'121'}

        self.assertCountEqual(Scheduler.get_courses_by_numbers(
            courses, course_numbers), [course_3])

    def test_get_courses_by_numbers_multiple_course_numbers_one_course_each_number(self):
        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [], None)
        course_2 = Course(2, '321', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [], None)
        course_3 = Course(3, '121', 'course 3', None, 4, [], None)
        course_4 = Course(4, '323', 'course 4', None, 4, [], None)

        courses = [course_1, course_2, course_3, course_4]
        course_numbers = {'121', '321'}

        self.assertCountEqual(Scheduler.get_courses_by_numbers(
            courses, course_numbers), [course_2, course_3])

    def test_get_courses_by_numbers_multiple_course_numbers_multiple_courses_each_number(self):
        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [], None)
        course_2 = Course(2, '321', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [], None)
        course_3 = Course(3, '121', 'course 3', None, 4, [], None)
        course_4 = Course(4, '323', 'course 4', None, 4, [], None)
        course_5 = Course(5, '123', 'course 1', Professor(
            'prof 1', 'prof_5@test.com'), 4, [], None)
        course_6 = Course(6, '321', 'course 2', Professor(
            'prof 2', 'prof_6@test.com'), 4, [], None)
        course_7 = Course(7, '121', 'course 3', None, 4, [], None)
        course_8 = Course(8, '323', 'course 4', None, 4, [], None)

        courses = [course_1, course_2, course_3, course_4,
                   course_5, course_6, course_7, course_8]
        course_numbers = {'121', '321'}

        self.assertCountEqual(Scheduler.get_courses_by_numbers(
            courses, course_numbers), [course_7, course_6, course_2, course_3])

    def test_is_valid_schedule_empty_schedule(self):
        self.assertTrue(Scheduler.is_valid_schedule([], 0))

    def test_is_valid_schedule_single_course(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], Final(datetime.date(2020, 12, 4), True, 60))

        self.assertTrue(Scheduler.is_valid_schedule([course_1], 0))

    def test_is_valid_schedule_single_course_no_final(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], None)

        self.assertTrue(Scheduler.is_valid_schedule([course_1], 0))


if __name__ == '__main__':
    unittest.main()
