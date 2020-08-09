from datetime import date


class Final:

    def __init__(self, date: date, isMorning: bool, code: int):
        self.date = date
        self.isMorning = isMorning
        self.code = code
