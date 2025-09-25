from persona import Persona

class Paziente(Persona):

    _idCode: str

    def __init__(self, first_name:str, last_name: str, idCode: str) -> None:
        super().__init__(first_name, last_name)
        self.setIdCode(idCode)

    def setIdCode(self, idCode: str) -> None:
        if not isinstance(idCode, str):
            raise ValueError("Codice identificativo deve essere una stringa")
        self._idCode = idCode

    def getidCode(self) -> str:
        return self._idCode
        
    def patienteInfo(self) -> str:
        print(f"Paziente: {self._first_name} {self._last_name}\nID: {self._idCode}")

    