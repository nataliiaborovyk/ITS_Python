'''
### Classi Person, Student e Lecturer:
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente

### Classe Group:
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.
'''


class Person:

    def __init__(self, cf:str, nome:str, cognome:str, eta:int) -> None:
        self.cf = cf
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
class Studente(Person):

    def __init__(self, cf:str, nome:str, cognome:str, eta:int) -> None:
        super().__init__(cf, nome, cognome, eta)
        self.group = None

    def set_group(self, group:"Group"):
        self.group = group

    def get_cognome(self) -> str:
        return self.cognome
    
class Lecturer(Person):

    def __init__(self, cf:str, nome:str, cognome:str, eta:int) -> None:
        super().__init__(cf, nome, cognome, eta)

class Group:

    def __init__(self, nome:str, limit:int, students:list[Studente] = None, lecturers:list[Lecturer] = None) -> None:
        self.nome = nome
        self.limit = limit
        self.students =  students or []
        self.lectures = lecturers or []
        self.corse = None

    def get_name(self) -> str:
        return self.nome
    
    def get_limit(self) -> int:
        return self.limit

    def get_students(self)-> list:
        return self.students
    
    def get_lectures(self) -> list:
        return self.lectures
    
    def get_limit_lecturers(self):
        limit_lectures = 0
        num_students = len(self.get_students())
        while num_students > 0:
            num_students -= 10
            limit_lectures += 1
        if limit_lectures < 1:
            return 1
        return limit_lectures
    
    def set_corse(self, corse: 'Cours') -> None:
        self.corse = corse

    
    def add_studente(self, student:Studente) -> None:
        if (len(self.get_students())) >= self.get_limit():
            raise ValueError("il massimo è aggiunto")
        if student in self.students:
            raise ValueError("gia presente")
        self.students.append(student)
        student.set_group(self)

    def add_lecture(self, lectur:Lecturer) -> None:
        if (len(self.get_lectures())) >= self.get_limit_lecturers():
            raise ValueError("il limite è raggiunto")
        if lectur in self.lectures:
            raise ValueError('gia presente')
        self.lectures.append(lectur)
        


'''
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso.
'''

class Cours:

    def __init__(self, nome:str, groups:list[Group] = None) -> None:
        self.nome = nome
        self.groups = groups or None

    def register(self, student:Studente) -> str:
        aggiunto:bool = False
        for gr in self.groups:
            if gr.get_limit() < len(gr.get_students()):
                if student not in gr:
                    gr.add_studente(student)
                    aggiunto = True
                    print(f"{student.get_cognome()}")
                    break
        if aggiunto == False:
            print('non ci sono posti')
            
    def get_groups(self) -> list:
        if not self.groups:
            return []
        return self.groups
    
    def add_group(self, group: Group) -> None:
        if group in self.groups:
            raise ValueError('gia presente')
        self.groups.append(group)
        group.set_corse(self)