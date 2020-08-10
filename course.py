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

    def __str__(self):
        return '''
            ID: {id}
            Number: {number}
            Title: {title}
            Professor: {professor}
            Units: {units}
            Sessions: {sessions}
            Final: {final}'''.format(
            id=self.id,
            number=self.number,
            title=self.title,
            professor=str(self.professor),
            units=self.units,
            sessions=str(self.sessions),
            final=str(self.final))
