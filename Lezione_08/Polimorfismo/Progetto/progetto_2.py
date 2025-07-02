'''
### Classi Person, Student e Lecturer:
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente

### Classe Group:
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), 
una lista di studenti (students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. 
            Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.
'''

class Person:

    def __init__(self, cf:str, name:str, surname:str, age:int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Group:

    def __init__(self, name:str, limit:int, students:list = None, lecturers:list = None):
        self.name = name
        self.limit = limit
        self.students = students if students is not None else []
        self.lecturers = lecturers if lecturers is not None else []

    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
        limit_lectures = 0
        num_students = self.limit
        while num_students > 0:
            num_students -= 10
            limit_lectures += 1
        return limit_lectures
    
    def add_student(self, student:'Student'):
        if len(self.students) < self.limit:
            if student not in self.students:
                self.students.append(student)
            else:
                print("è gia nel gruppo")
        else:
            print("il gruppo è pieno")

    def add_lecturer(self, lecturer:'Lecturer'):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
        else:
            print("Limite docenti è raggiunto")

class Student(Person):
    
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group:Group): 
        if len(group.get_students()) < group.get_limit():
            self.group = group
            group.add_student(self)
        else:
            print("gruppo è pieno")

class Lecturer(Person):
    
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        

# Creazione delle persone
person1 = Person(cf="CF123", name="John", surname="Doe", age=30)
student1 = Student(cf="CF456", name="Jane", surname="Smith", age=20)
lecturer1 = Lecturer(cf="CF789", name="Dr. Emily", surname="Brown", age=45)

# Test della classe Person
print("Test della classe Person:")
print(f"CF: {person1.cf}, Atteso: CF123")
print(f"Nome: {person1.name}, Atteso: John")
print(f"Cognome: {person1.surname}, Atteso: Doe")
print(f"Età: {person1.age}, Atteso: 30")

# Test della classe Student
print("\nTest della classe Student:")
print(f"CF: {student1.cf}, Atteso: CF456")
print(f"Nome: {student1.name}, Atteso: Jane")
print(f"Cognome: {student1.surname}, Atteso: Smith")
print(f"Età: {student1.age}, Atteso: 20")
print(f"Gruppo iniziale: {student1.group}, Atteso: None")

# Test metodo set_group della classe Student
group1 = Group(name="Group A", limit=10)
student1.set_group(group1)
print("\nDopo set_group di student1:")
print(f"Gruppo di student1: {student1.group.get_name()}, Atteso: Group A")

# Test della classe Lecturer
print("\nTest della classe Lecturer:")
print(f"CF: {lecturer1.cf}, Atteso: CF789")
print(f"Nome: {lecturer1.name}, Atteso: Dr. Emily")
print(f"Cognome: {lecturer1.surname}, Atteso: Brown")
print(f"Età: {lecturer1.age}, Atteso: 45")

# Creazione di un gruppo e aggiunta di studenti e docenti
group2 = Group(name="Group B", limit=2)
group2.add_student(student1)
group2.add_lecturer(lecturer1)

print("\nDopo aggiunta di student1 e lecturer1 a group2:")
print(f"Studenti in group2: {[student.cf for student in group2.get_students()]}, Atteso: [CF456]")
print(f"Docenti in group2: {[lecturer.cf for lecturer in group2.lecturers]}, Atteso: [CF789]")