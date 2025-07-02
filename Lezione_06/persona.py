class Persona:
    '''
    nome, cognome e eta sono gli atributi della classe persona, questi atributi saranno chiamati
    self.name:str, self.cognome:str, self.age:int
    '''
    #costruttore
    def __init__(self, name:str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age