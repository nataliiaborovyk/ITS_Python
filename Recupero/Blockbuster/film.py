from __future__ import annotations
from abc import ABC, abstractmethod

class Film:

    _id: int
    _title: str

    def __init__(self, id: int, title: str) -> None:

        self.setID(id)
        self.setTitle(title)

    def setID(self, id: int) -> None:
        self._id = id

    def setTitle(self, title) -> None:
        self._title = title

    def getID(self) -> int:
        return self._id
    
    def getTitle(self) -> str:
        return self._title
    
    def isEqual(self, otherFilm: Film) -> bool:
        return self._id == otherFilm.getID()
    
    @abstractmethod
    def getGenere(self) -> str:
        pass

    @abstractmethod
    def getPenale(self) -> float:
        pass

    @abstractmethod
    def calcolaPenaleRitardo(self, giorni: int) -> float:
        pass