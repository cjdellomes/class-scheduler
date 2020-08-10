class Professor:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return '''
            name: {name}
            email: {email}'''.format(
            name=self.name,
            email=self.email)
