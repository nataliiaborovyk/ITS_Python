class Persona:

    def __init__(self, name:str, lastname:str, age:int):
        self.setName(name)
        self.setLastName(lastname)
        self.setAge(age)

    def setName(self, name:str):
        if name:
            self.name = name
        else:
            print("Error")
    
    def setLastName(self, lastname:str):
        if lastname:
            self.lastname = lastname
        else:
            print("Error! Il cognome non puo essere una stringa vuota!")

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
    
    def speak(self) -> None:
        print(f"\nHello! my name is {self.getName()}!\n")
    
