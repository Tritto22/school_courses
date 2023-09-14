from datetime import datetime
class Person:
    def __init__(self, name, surname, birthDate, univoqueCode):
        self.name=name
        self.surname=surname
        if self.__validation_date(birthDate):
            self.birthDate=birthDate
        else:
            raise TypeError('Data non valida')
        self.univoqueCode=univoqueCode

    def __validation_date(self, birthDate):
        return isinstance(birthDate, datetime) and birthDate<datetime.now()
        

    @property
    def age(self):
        age=int((datetime.now()-self.birthDate).days/365)
        return age
    
    @property
    def maggiorenne(self):
        return self.age>=18         # chiama property age con .age


# *********Esempio aggiunta Person con costrutto try except
# try:
#     gigi=Person('Gigi', 'Rossi', datetime(1995, 12, 21), 1)
#     print(f'{gigi.name} ha {gigi.age} anni')
# except:
#     print('Errore')

# **********Esempio aggiunta Person
# data_nascita=datetime(1999,10,20)
# pp=Person('Luigi','Bianchi', data_nascita, 1)