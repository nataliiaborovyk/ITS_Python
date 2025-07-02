class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

    #funzione che mostra in output i dati di una persona
    def displayData(self) -> None:
        print(f"Nome:{self.name}\nCognome: {self.lastname}\nEta: {self.age}")

    #funzione che ci consenta di impostare un valore di self.name
    def setName(self, name:str) -> None:
        self.name = name

    #funzione che ci consenta di impostare il valore self.lastname
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname

    #funzione che imposta age
    def setAge(self, age:int) -> None:
        #self.age = age
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    #funzione che consente di ritornare il valore di set.name
    def getName(self) -> str:
        return self.name
    
    #funz. che consente di ritornare il valore si self.lastname
    def getLastname(self) -> str:
        return self.lastname
    
    #funz. che consente di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age
