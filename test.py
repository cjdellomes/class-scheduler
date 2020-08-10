from scheduler import Scheduler
from professor import Professor
from course import Course
from final import Final
from session import Session
import datetime
import unittest


class TestScheduler(unittest.TestCase):

    def test_scheduler(self):
        course_1 = Course(1, '201', 'test1', None, 4, [
            Session(1, datetime.time(13, 45, 0), datetime.time(15, 0, 0)),
            Session(2, datetime.time(13, 45, 0), datetime.time(15, 0, 0)),
            Session(3, datetime.time(13, 45, 0), datetime.time(15, 0, 0)),
        ], Final(datetime.date(2020, 12, 14), True, 70))
        course_2 = Course(2, '202', 'test2', None, 4, [
            Session(1, datetime.time(8, 45, 0), datetime.time(10, 0, 0)),
            Session(3, datetime.time(8, 45, 0), datetime.time(10, 0, 0)),
            Session(5, datetime.time(8, 45, 0), datetime.time(10, 0, 0)),
        ], None)
        course_3 = Course(3, '202', 'test2', None, 4, [
            Session(1, datetime.time(9, 0, 0), datetime.time(10, 15, 0)),
            Session(3, datetime.time(9, 0, 0), datetime.time(10, 15, 0)),
            Session(5, datetime.time(9, 0, 0), datetime.time(10, 15, 0)),
        ], Final(datetime.date(2020, 12, 16), True, 73))
        course_4 = Course(4, '205', 'test3', None, 4, [
            Session(1, datetime.time(10, 45, 0), datetime.time(12, 0, 0)),
            Session(2, datetime.time(10, 45, 0), datetime.time(12, 0, 0)),
            Session(4, datetime.time(10, 45, 0), datetime.time(12, 0, 0)),
        ], Final(datetime.date(2020, 12, 8), True, 64))

        courses = [course_1, course_2, course_3, course_4]
        max_units = 20
        course_numbers = {'201', '202', '205'}
        min_days_between_finals = 0

        self.assertEqual(len(Scheduler.get_schedules(
            courses, max_units, course_numbers, min_days_between_finals)), 2)

    def test_scheduler_empty_course_list(self):
        courses = []
        max_units = 20
        course_numbers = {'100', '200', '300'}
        min_days_between_finals = 1
        self.assertEqual(Scheduler.get_schedules(
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

    def test_is_valid_schedule_same_session_times(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_5 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_6 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], None)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5, session_6], None)

        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 0))

    def test_is_valid_schedule_overlapping_session_times(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(1, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_5 = Session(2, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_6 = Session(3, datetime.time(
            15, 45, 0), datetime.time(15, 0, 0))

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], None)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5, session_6], None)

        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 0))

    def test_is_valid_schedule_one_overlapping_session_time(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(3, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_5 = Session(4, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_6 = Session(5, datetime.time(
            15, 45, 0), datetime.time(15, 0, 0))

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], None)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5, session_6], None)

        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 0))

    def test_is_valid_schedule_no_overlapping_session_times(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(4, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))
        session_5 = Session(5, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], None)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5], None)

        self.assertTrue(Scheduler.is_valid_schedule([course_1, course_2], 0))

    def test_is_valid_schedule_back_to_back_session_times(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(1, datetime.time(
            15, 0, 0), datetime.time(16, 0, 0))
        session_5 = Session(2, datetime.time(
            15, 0, 0), datetime.time(16, 0, 0))
        session_6 = Session(3, datetime.time(
            15, 0, 0), datetime.time(16, 0, 0))

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], None)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5, session_6], None)

        self.assertTrue(Scheduler.is_valid_schedule([course_1, course_2], 0))

    def test_is_valid_schedule_same_day_finals_no_overlapping_session_times(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(4, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))
        session_5 = Session(5, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))

        final_1 = Final(datetime.date(2020, 12, 4), True, 60)
        final_2 = Final(datetime.date(2020, 12, 4), True, 60)

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], final_1)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5], final_2)

        self.assertTrue(Scheduler.is_valid_schedule([course_1, course_2], 0))
        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 1))

    def test_is_valid_schedule_different_day_finals_no_overlapping_session_times(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(4, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))
        session_5 = Session(5, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))

        final_1 = Final(datetime.date(2020, 12, 4), True, 60)
        final_2 = Final(datetime.date(2020, 12, 5), True, 60)

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], final_1)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5], final_2)

        self.assertTrue(Scheduler.is_valid_schedule([course_1, course_2], 0))
        self.assertTrue(Scheduler.is_valid_schedule([course_1, course_2], 1))
        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 2))
        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 3))

    def test_is_valid_schedule_same_day_finals_overlapping_session_times(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(1, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_5 = Session(2, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_6 = Session(3, datetime.time(
            15, 45, 0), datetime.time(15, 0, 0))

        final_1 = Final(datetime.date(2020, 12, 4), True, 60)
        final_2 = Final(datetime.date(2020, 12, 4), True, 60)

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], final_1)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5, session_6], final_2)

        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 0))
        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 1))

    def test_is_valid_schedule_different_day_finals_overlapping_session_times(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(1, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_5 = Session(2, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_6 = Session(3, datetime.time(
            15, 45, 0), datetime.time(15, 0, 0))

        final_1 = Final(datetime.date(2020, 12, 4), True, 60)
        final_2 = Final(datetime.date(2020, 12, 5), True, 60)

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], final_1)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5, session_6], final_2)

        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 0))
        self.assertFalse(Scheduler.is_valid_schedule([course_1, course_2], 1))

    def test_is_valid_schedule_different_day_finals_one_overlapping_session_time(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(3, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))
        session_5 = Session(4, datetime.time(
            14, 45, 0), datetime.time(15, 0, 0))
        session_6 = Session(5, datetime.time(
            15, 45, 0), datetime.time(15, 0, 0))
        session_7 = Session(5, datetime.time(
            8, 0, 0), datetime.time(13, 0, 0))

        final_1 = Final(datetime.date(2020, 12, 4), True, 60)
        final_2 = Final(datetime.date(2020, 12, 5), True, 60)
        final_3 = Final(datetime.date(2020, 12, 6), True, 60)

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], final_1)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5, session_6], final_2)
        course_3 = Course(3, '123', 'course 3', Professor(
            'prof 3', 'prof_3@test.com'), 4, [session_7], final_3)

        self.assertFalse(Scheduler.is_valid_schedule(
            [course_1, course_2, course_3], 0))
        self.assertFalse(Scheduler.is_valid_schedule(
            [course_1, course_2, course_3], 1))
        self.assertFalse(Scheduler.is_valid_schedule(
            [course_1, course_2, course_3], 2))

    def test_is_valid_schedule_same_and_different_day_finals_no_overlapping_session_time(self):
        session_1 = Session(1, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_2 = Session(2, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_3 = Session(3, datetime.time(
            13, 45, 0), datetime.time(15, 0, 0))
        session_4 = Session(4, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))
        session_5 = Session(5, datetime.time(
            14, 45, 0), datetime.time(16, 0, 0))
        session_6 = Session(5, datetime.time(
            8, 0, 0), datetime.time(13, 0, 0))

        final_1 = Final(datetime.date(2020, 12, 4), True, 60)
        final_2 = Final(datetime.date(2020, 12, 5), True, 60)
        final_3 = Final(datetime.date(2020, 12, 5), True, 60)

        course_1 = Course(1, '123', 'course 1', Professor(
            'prof 1', 'prof_1@test.com'), 4, [session_1, session_2, session_3], final_1)
        course_2 = Course(2, '123', 'course 2', Professor(
            'prof 2', 'prof_2@test.com'), 4, [session_4, session_5], final_2)
        course_3 = Course(3, '123', 'course 3', Professor(
            'prof 3', 'prof_3@test.com'), 4, [session_6], final_3)

        self.assertTrue(Scheduler.is_valid_schedule(
            [course_1, course_2, course_3], 0))
        self.assertFalse(Scheduler.is_valid_schedule(
            [course_1, course_2, course_3], 1))
        self.assertFalse(Scheduler.is_valid_schedule(
            [course_1, course_2, course_3], 2))


if __name__ == '__main__':
    unittest.main()
