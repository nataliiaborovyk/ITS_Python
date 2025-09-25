
from paziente import Paziente
from dottore import Dottore


class Fattura:

    _pazient: list[Paziente]
    _doctor: Dottore
    _fatture: int
    _salary: int

    def __init__(self, doctor: Dottore, pazient: Paziente) -> None:
        if doctor.isValidDoctor():
            self._fatture = len(pazient)
            self._salary = 0
            self._pazient = pazient
            self._doctor = doctor
        else:
            self._pazient = None
            self._doctor = None
            self._fatture = None
            self._salary = None
            raise ValueError("Non è possibile creare la classe fattura poichè il dottore non è valido!")
        
        
        
    def getSalary(self) -> int:
        self._salary = self._doctor.getParcel() * len(self._pazient)
        return self._salary
    
    def getFatture(self) -> int:
        self._fatture = len(self._pazient)
        return self._fatture
    
    def addPatient(self, newPatient: Paziente) -> str:
        if newPatient in self._pazient:
            raise ValueError("Il Paziente è gia nella lista")
        self._pazient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor cognome è stato aggiunto il paziente {newPatient.getidCode()}")

    def removePatient(self, idCode: str) -> str:
        for i in self._pazient:
            if i.getidCode() == idCode:
                self._pazient.remove(i)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor cognome è stato rimosso il paziente {idCode}")


