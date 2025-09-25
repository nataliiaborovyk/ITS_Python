from persona import Persona

class Dottore(Persona):

    _specialization: str
    _parcel: float

    def __init__(self, first_name:str, last_name: str, 
                 specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        if type(specialization) is not str:
            specialization = None
            raise ValueError("La specializazione inserita non è una str")
        if type(parcel) is not float:
            parcel = None
            raise ValueError("La parcella inserita non è un float!")
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    def setSpecialization(self, specialization: str) -> None:
        if type(specialization) is not str:
            raise ValueError("La specializazione inserita non è una str")
        self._specialization = specialization

    def setParcel(self, parcel: float) -> None:
        if type(parcel) is not float:
            raise ValueError("La parcella inserita non è un float!")
        self._parcel = parcel

    def getSpecialization(self) -> str | None:
        return self._specialization
    
    def getParcel(self) -> float:
        return self._parcel
    
    def isValidDoctor(self) -> bool:
        if self._age > 30:
            print("Doctor nome e cognome is valid!")
            return True
        else:
            print("Doctor nome e cognome is not valid!")
            return False

    def doctorGreet(self) -> str:
        super().greet()
        print(f"Sono un medico {self._specialization}")