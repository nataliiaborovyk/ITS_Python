class Persona:

    def __init__(self, name:str, lastname:str, age:int):
        self.name = ""
        self.lastname = ""
        self.age = 0

    def setName(self, name:str):
        if name:
            self.name = name
        else:
            print("Error")
    
    def setLastName(self, lastname:str):
        self.lastname = lastname

    def setAge(self, age:int):
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    def getName(self):
        return self.name
    
    def getLastName(self):
        return self.lastname
    
    def getAge(self):
        return self.age
    
    def __str__(self) -> str:
        return f" Name:  {self.name}\n Surname: {self.lastname}\n Age: {self.age}"
    
