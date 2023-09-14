from person import Person

class Student(Person):
    def __init__(self, name, surname, birthDate, univoqueCode):
        super().__init__(name, surname, birthDate, univoqueCode)

