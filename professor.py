from person import Person

class Professor(Person):
    def __init__(self, name, surname, birthDate, univoqueCode, degree):
        super().__init__(name, surname, birthDate, univoqueCode)
        self.degree=degree

