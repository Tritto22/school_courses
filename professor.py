from person import Person

class Professor(Person):
    def __init__(self, name, surname, age, univoqueCode, degree):
        super().__init__(name, surname, age, univoqueCode)
        self.degree=degree

