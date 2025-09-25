

class Persona:

    _first_name: str
    _last_name: str
    _age: int

    def __init__(self, first_name: str, last_name: str) -> None:
        if type(first_name) is not str:
            first_name = None
            raise ValueError("Il nome inserito non è una stringa!")
        if type(last_name) is not str:
            last_name = None
            raise ValueError("Il cognome inserito non è una stringa!")
        if type(first_name) is str and type(last_name) is str:
            self._age = 0
        else:
            age = None
        self.setName(first_name)
        self.setLastName(last_name)

    def setName(self, first_name: str) -> None:
        if type(first_name) is not str:
            raise ValueError("Il nome inserito non è una stringa!")
        self._first_name = first_name

    def setLastName(self, last_name: str) -> None:
        if type(last_name) is not str:
            raise ValueError("Il cognome inserito non è una stringa!")
        self._last_name = last_name

    def setAge(self, age: int) -> None:
        if type(age) is not int:
            raise ValueError("L'età deve essere un numero intero!")
        self._age = age

    def getName(self) -> str | None:
        return self._first_name
    
    def getLastName(self) -> str | None:
        return self._last_name
    
    def getAge(self) -> int:
        return self._age
    
    def greet(self) -> str:
        print(f"Ciao, sono {self._first_name} {self._last_name}! Ho {self._age} anni!")




