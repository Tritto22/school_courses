from person import Person

class Professor(Person):
    def __init__(self, name, surname, age, univoqueCode, degree):
        super().__init__(name, surname, age, univoqueCode)
        self.degree=degree


# Esempio aggiunta docenti
p1=Professor('Nicola', 'Ilgrande', 88, 1, 'Storia')
p2=Professor('Simona', 'Boccabella', 21, 2, 'Arte')
p3=Professor('Rita', 'Gliato', 19, 3, 'Cucito')
p4=Professor('Anna', 'Rota', 22, 4, 'Aerobica')
p5=Professor('Giovanni', 'Allevi', 26, 5, 'Sostegno')