from person import Person

class Student(Person):
    def __init__(self, name, surname, age, univoqueCode):
        super().__init__(name, surname, age, univoqueCode)



# Esempio aggiunta studenti
s1=Student('Giovanni', 'Pezzocchia', 20, 1)
s2=Student('Andrea', 'Mastrogiacomo', 21, 2)
s3=Student('Gino', 'Pappalardo', 19, 3)
s4=Student('Danilo', 'Fratannera', 22, 4)
s5=Student('Peppe', 'Reppe', 26, 5)