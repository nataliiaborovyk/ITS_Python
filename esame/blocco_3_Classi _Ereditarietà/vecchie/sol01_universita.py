from __future__ import annotations  # Permette riferimenti a classi non ancora definite (per Python < 3.10)
from abc import ABC, abstractmethod  # Moduli per la creazione di classi astratte

# Classe astratta che rappresenta una persona generica
class Person(ABC):
    def __init__(self, name:str, age:int) -> None:
        self.name:str = name  # Nome della persona
        self.age:int = age    # Età della persona

    @abstractmethod
    def get_role(self) -> str:
        pass  # Metodo astratto da implementare nelle sottoclassi

    def __str__(self) -> str:
        # Rappresentazione stringa dell'oggetto Person
        return f"Name: {self.name}, Age: {self.age}, Role: {self.get_role()}"

# Sottoclasse che rappresenta uno Studente
class Student(Person):
    def __init__(self, name:str, age:int, student_id:str) -> None:
        super().__init__(name, age)  # Inizializza nome e età dalla superclasse
        self.student_id:str = student_id  # ID dello studente
        self.courses:list[Course] = []    # Lista dei corsi frequentati

    def get_role(self) -> str:
        return "Student"  # Implementazione del metodo astratto

    def enroll(self, course:Course) -> None:
        # Iscrive lo studente al corso se non già presente
        if course not in self.courses:
            self.courses.append(course)

    def __str__(self) -> str:
        # Estende la rappresentazione stringa con l'ID dello studente
        return super().__str__() + f"ID: {self.student_id}"

# Sottoclasse che rappresenta un Professore
class Professor(Person):
    def __init__(self, name:str, age:int, professor_id:str) -> None:
        super().__init__(name, age)
        self.professor_id:str = professor_id
        self.department:Department = None  # Dipartimento associato (inizialmente None)
        self.courses:list[Course] = []     # Corsi tenuti dal professore

    def get_role(self) -> str:
        return "Professor"

    def assign_to_course(self, course:Course) -> None:
        # Assegna un corso al professore
        if course not in self.courses:
            self.courses.append(course)

    def set_department(self, department:Department) -> None:
        self.department = department  # Imposta il dipartimento

    def __str__(self) -> str:
        # Se ha un dipartimento, lo include nella stringa, altrimenti mostra un messaggio predefinito
        if self.department:
            department_name:str = self.department.department_name
            return super().__str__() + f"ID: {self.professor_id}, Department: {department_name}, Courses: {[c.course_name for c in self.courses]}"
        else:
            return super().__str__() + f"ID: {self.professor_id}, Department: 'Dipartimento non ancora assegnato'"

# Classe che rappresenta un Corso universitario
class Course:
    def __init__(self, name:str, code:str) -> None:
        self.course_name:str = name      # Nome del corso
        self.course_code:str = code      # Codice identificativo
        self.students:list[Student] = [] # Studenti iscritti al corso
        self.professor:Professor = None  # Professore assegnato

    def add_student(self, student:Student) -> None:
        if student not in self.students:
            self.students.append(student)

    def set_professor(self, professor:Professor) -> None:
        self.professor = professor  # Imposta il professore

    def __str__(self) -> str:
        # Rappresentazione del corso con elenco studenti e professore
        if self.professor:
            professor_name:str = self.professor.name
            return f"Course name: {self.course_name}, Course ID: {self.course_code}, Professor: {professor_name}, Students: {[s.name for s in self.students]}"
        else:
            return f"Course name: {self.course_name}, Course ID: {self.course_code}, Professor: 'Non ancora assegnato'"

# Classe che rappresenta un Dipartimento universitario
class Department:
    def __init__(self, name:str) -> None:
        self.department_name:str = name       # Nome del dipartimento
        self.professors:list[Professor] = []  # Lista dei professori associati
        self.courses:list[Course] = []        # Lista dei corsi offerti

    def add_course(self, course:Course) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def add_professor(self, professor:Professor) -> None:
        if professor not in self.professors:
            self.professors.append(professor)

    def __str__(self) -> str:
        return f'Department: {self.department_name}, Course: {[c.course_name for c in self.courses]}, Professors: {[p.name for p in self.professors]}'

# Classe che rappresenta un'Università
class University:
    def __init__(self, name:str) -> None:
        self.university_name:str = name         # Nome dell'università
        self.departments:list[Department] = []  # Elenco dei dipartimenti
        self.students:list[Student] = []        # Elenco degli studenti iscritti

    def add_department(self, department:Department) -> None:
        self.departments.append(department)

    def add_student(self, student:Student) -> None:
        self.students.append(student)

    def __str__(self) -> str:
        return f'University: {self.university_name}, Departments: {[d.department_name for d in self.departments]}, Students: {[s.name for s in self.students]}'

# Blocco di esecuzione principale
if __name__ == '__main__':
    univ:University = University("Sapienza")  # Crea un'università

    # Crea e aggiunge i dipartimenti
    cs_dep:Department = Department('Informatica')
    lt_dep:Department = Department('Lettere')
    univ.add_department(cs_dep)
    univ.add_department(lt_dep)

    # Crea i corsi
    python_cs:Course = Course("Programmazione in Python", "PY101")
    antica_cs:Course = Course("Lettere antiche", "LT101")
    cs_dep.add_course(python_cs)
    lt_dep.add_course(antica_cs)

    # Crea i professori
    mc_prof:Professor = Professor("Marco Cascio", 18, "MC100")
    me_prof:Professor = Professor("Marco Esposito", 30, "ME150")
    cs_dep.add_professor(mc_prof)
    lt_dep.add_professor(me_prof)
    mc_prof.set_department(cs_dep)
    me_prof.set_department(lt_dep)
    mc_prof.assign_to_course(python_cs)
    me_prof.assign_to_course(antica_cs)
    python_cs.set_professor(mc_prof)
    antica_cs.set_professor(me_prof)

    # Crea e iscrive gli studenti
    student_leandro:Student = Student("Leandro Pazienza", 27, "PZN")
    student_cristiano:Student = Student("Cristiano Coccia", 21, "CR7")
    univ.add_student(student_leandro)
    univ.add_student(student_cristiano)
    student_cristiano.enroll(python_cs)
    student_leandro.enroll(antica_cs)
    python_cs.add_student(student_cristiano)
    antica_cs.add_student(student_leandro)

    # Stampa lo stato dell'università, dei dipartimenti, dei corsi e dei partecipanti
    print(univ)
    print(cs_dep)
    print(lt_dep)
    print(python_cs)
    print(antica_cs)
    print(mc_prof)
    print(me_prof)