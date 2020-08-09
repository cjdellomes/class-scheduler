from course import Course


class Scheduler:

    @staticmethod
    def get_schdeules(courses: list,
                      max_units: int,
                      course_numbers: set,
                      min_days_between_finals: int):
        result = []
        possible_courses = get_courses_by_numbers(courses, course_numbers)
        get_schedules_helper(possible_courses, max_units, course_numbers,
                             days_between_finals, [], result)
        return result

    @staticmethod
    def get_schedules_helper(courses: list,
                             curr_units: int,
                             remaining_course_numbers: set,
                             min_days_between_finals: int,
                             curr_schedule: list,
                             result: list):
        if curr_units < 0 or not is_valid_schedule(curr_schedule, min_days_between_finals):
            return
        if len(remaining_course_numbers) == 0:
            result.append(curr_schedule)
            return

        for course in courses:
            if course.number in remaining_course_numbers:
                curr_units -= course.units
                curr_schedule.append(course)
                remaining_course_numbers.remove(course.number)

                get_schedules_helper(courses, curr_units, remaining_course_numbers,
                                     min_days_between_finals, curr_schedule, result)

                curr_schedule.pop()
                curr_units += course.units
                remaining_course_numbers.add(course.number)

    @staticmethod
    def get_courses_by_numbers(courses: list, course_numbers: set):
        result = []
        for course in courses:
            if course.number in course_numbers:
                result.append(course)
        return result

    @staticmethod
    def is_valid_schedule(courses, min_days_between_finals):
        sessions = []
        finals = []
        for course in courses:
            finals.append(course.final)
            for session in course.sessions:
                sessions.append(sessions)

        sessions.sort(key=lambda x: (x.day_of_week, x.start_time))
        for i in range(1, len(sessions)):
            if sessions[i].day_of_week == sessions[i - 1].day_of_week and sessions[i].start_time > sessions[i - 1].end_time:
                return False

        finals.sort(key=lambda x: x.date)
        for i in range(1, len(finals)):
            if (finals[i] - finals[i - 1]).days < min_days_between_finals:
                return False

        return True
