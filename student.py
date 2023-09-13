from person import Person

class Student(Person):
    def __init__(self, name, surname, age, univoqueCode):
        super().__init__(name, surname, age, univoqueCode)

