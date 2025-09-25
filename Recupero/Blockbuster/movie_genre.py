from __future__ import annotations

from film import Film
    
class Azione(Film):

    _genere: str
    _penale: float

    def __init__(self, id:int, title: str) -> None:
        super().__init__(id, title)
        self._penale: float = 3.0
        self._genere = "Azione"

    def getGenere(self) -> str:
        return self._genere
    
    def getPenale(self) -> float:
        return self._penale
    
    def calcolaPenaleRitardo(self, giorni: int) -> float:
        return self._penale * giorni
    

class Commedia(Film):

    _genere: str
    _penale: float

    def __init__(self, id:int, title: str) -> None:
        super().__init__(id, title)
        self._penale: float = 2.5
        self._genere = "Commedia"

    def getGenere(self) -> str:
        return self._genere
    
    def getPenale(self) -> float:
        return self._penale
    
    def calcolaPenaleRitardo(self, giorni: int) -> float:
        return self._penale * giorni


class Dramma(Film):

    _genere: str
    _penale: float

    def __init__(self, id:int, title: str) -> None:
        super().__init__(id, title)
        self._penale: float = 2.0
        self._genere = "Dramma"

    def getGenere(self) -> str:
        return self._genere
    
    def getPenale(self) -> float:
        return self._penale
    
    def calcolaPenaleRitardo(self, giorni: int) -> float:
        return self._penale * giorni   