from datetime import datetime
class Person:
    def __init__(self, name, surname, birthDate, univoqueCode):
        self.name=name
        self.surname=surname
        self.birthDate=birthDate
        self.univoqueCode=univoqueCode

    @property
    def age(self):
        age=int((datetime.now()-self.birthDate).days/365)
        return age
    
    @property
    def maggiorenne(self):
        return self.age>=18         # chiama property age con .age


# Esempio aggiunta Person
# data_nascita=datetime(1999,10,20)
# pp=Person('Luigi','Bianchi', data_nascita, 1)