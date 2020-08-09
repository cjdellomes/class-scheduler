from professor import Professor
from session import Session
from final import Final


class Course:

    def __init__(self, id, number, title, professor, units, sessions, final):
        self.id = id
        self.number = number
        self.title = title
        self.professor = professor
        self.units = units
        self.sessions = sessions
        self.final = final
