from datetime import time


class Session:

    def __init__(self, day_of_week: int, start_time: time, end_time: time):
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return '''
            Day of Week: {day_of_week}
            Start Time: {start_time}
            End Time: {end_time}'''.format(
            day_of_week=self.day_of_week,
            start_time=self.start_time,
            end_time=self.end_time)
