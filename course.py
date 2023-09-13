from student import Student
from professor import Professor
from random import choice as c

class Course:
    def __init__(self, name, professor):
        self.name=name
        self.professor=professor
        self.students=[]
        self.course=dict()
        self.__make_id()

    def __make_id(self):
        self.id=str(self.name[0:3].upper()+str(c(range(1111,9999))))

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, professor):
        if self.name in self.course:
            self.course[self.name].append(professor, self.students)
        else:
            self.course[self.name] = [professor, self.students]

    def show_course(self):
        for key, value in self.course.items():
            print(f'Nome del corso: {key} \nTenuto dal docente {value[0].name} {value[0].surname}\nAlunni iscritti:')
            for student in value[1]:
                print(f'\t{student.name} {student.surname} id:{student.univoqueCode}\n')

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