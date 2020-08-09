from datetime import time


class Session:

    def __init__(self, day_of_week: int, start_time: time, end_time: time):
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time
