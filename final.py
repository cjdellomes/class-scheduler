from datetime import date


class Final:

    def __init__(self, date: date, isMorning: bool, code: int):
        self.date = date
        self.isMorning = isMorning
        self.code = code

    def __str__(self):
        return '''
            Date: {date}
            Is Monring: {isMorning}
            Code: {code}'''.format(
            date=self.date,
            isMorning=self.isMorning,
            code=self.code)
