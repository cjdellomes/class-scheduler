import datetime


class ClassSession:

    def __init__(self, day_of_week, start_time, end_time):
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time


class Schedule:

    def __init__(self, class_sessions):
        self.class_sessions = class_sessions


class Final:

    def __init__(self, date, isMorning, code):
        self.date = date
        self.isMorning = isMorning
        self.code = code


class Professor:

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Course:

    def __init__(self, id, number, title, professor, units, schedule, final):
        self.id = id
        self.number = number
        self.title = title
        self.professor = professor
        self.units = units
        self.schedule = schedule
        self.final = final
