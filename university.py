from student import Student
from professor import Professor
from course import Course

class University:
    def __init__(self, name):
        self.name=name
        self.courses=dict()

    def add_course(self, course):
        if course.name in self.courses:
            print('Errore, esiste già un corso con l\'identificativo '+course.id)
        else:
            self.courses[course.id] = [course]

    def number_of_courses(self):
        return print(f'Il numero di corsi per l\'Università {self.name} è pari a {len(self.courses)}')

# Esempio aggiunta università
u1=University('Arizona University')

# Esempio aggiunta studenti
s1=Student('Giovanni', 'Pezzocchia', 20, 1)
s2=Student('Andrea', 'Mastrogiacomo', 21, 2)
s3=Student('Gino', 'Pappalardo', 19, 3)
s4=Student('Danilo', 'Fratannera', 22, 4)
s5=Student('Peppe', 'Reppe', 26, 5)

# Esempio aggiunta docenti
p1=Professor('Nicola', 'Ilgrande', 88, 1, 'Storia')
p2=Professor('Simona', 'Boccabella', 21, 2, 'Arte')
p3=Professor('Rita', 'Gliato', 19, 3, 'Cucito')
p4=Professor('Anna', 'Rota', 22, 4, 'Aerobica')
p5=Professor('Giovanni', 'Allevi', 26, 5, 'Sostegno')

# Esempio aggiunta corsi:
c1=Course('Storia', p1)
c2=Course('Arte', p2)
c3=Course('Aerobica', p4)