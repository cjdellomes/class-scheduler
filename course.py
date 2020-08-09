from professor import Professor
from session import Session
from final import Final


class Course:

    def __init__(self, id: int,
                 number: str,
                 title: str,
                 professor: Professor,
                 units: int,
                 sessions: list,
                 final: Final):
        self.id = id
        self.number = number
        self.title = title
        self.professor = professor
        self.units = units
        self.sessions = sessions
        self.final = final
