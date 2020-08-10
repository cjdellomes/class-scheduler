from course import Course
import datetime


class Scheduler:

    @staticmethod
    def get_schedules(courses: list,
                      max_units: int,
                      course_numbers: set,
                      min_days_between_finals: int):
        result = []
        possible_courses = Scheduler.get_courses_by_numbers(
            courses, course_numbers)

        Scheduler.get_schedules_helper(possible_courses, max_units, course_numbers,
                                       min_days_between_finals, [], result)
        return result

    @staticmethod
    def get_schedules_helper(courses: list,
                             curr_units: int,
                             remaining_course_numbers: set,
                             min_days_between_finals: int,
                             curr_schedule: list,
                             result: list):
        if curr_units < 0 or not Scheduler.is_valid_schedule(curr_schedule, min_days_between_finals):
            return
        if len(remaining_course_numbers) == 0:
            result.append(curr_schedule.copy())
            return

        for course in courses:
            if course.number not in remaining_course_numbers:
                continue

            curr_units -= course.units
            curr_schedule.append(course)
            remaining_course_numbers.remove(course.number)

            Scheduler.get_schedules_helper(courses, curr_units, remaining_course_numbers,
                                           min_days_between_finals, curr_schedule, result)

            remaining_course_numbers.add(course.number)
            curr_schedule.pop()
            curr_units += course.units

    @staticmethod
    def get_courses_by_numbers(courses: list, course_numbers: set):
        result = []
        for course in courses:
            if course.number in course_numbers:
                result.append(course)
        return result

    @staticmethod
    def is_valid_schedule(courses: list, min_days_between_finals: int):
        sessions = []
        finals = []
        min_date = datetime.date(1970, 1, 1)
        for course in courses:
            finals.append(course.final)
            for session in course.sessions:
                sessions.append(session)

        sessions.sort(key=lambda x: (x.day_of_week, x.start_time))
        for i in range(1, len(sessions)):
            if sessions[i].day_of_week == sessions[i - 1].day_of_week and sessions[i].start_time < sessions[i - 1].end_time:
                return False

        finals.sort(key=lambda x: x.date if x else min_date)
        for i in range(1, len(finals)):
            if finals[i] is None or finals[i - 1] is None or finals[i].date == min_date or finals[i - 1].date == min_date:
                continue
            if (finals[i].date - finals[i - 1].date).days < min_days_between_finals:
                return False

        return True
