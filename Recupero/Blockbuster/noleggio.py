from __future__ import annotations

from film import Film
from movie_genre import Azione, Dramma, Commedia

class Noleggio:

    _film_list: list[Azione | Dramma | Commedia]
    _rented_film: dict[int, list[Azione | Dramma | Commedia]]

    def __init__(self, film_list: list[Azione | Dramma | Commedia]) -> None:
        self._rented_film: dict[int, list[Azione | Dramma | Commedia]] = {}
        self._film_list = film_list

    def isAvaible(self, film: Azione | Dramma | Commedia) -> bool:
        if film in self._film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
        
    def rentAMovie(self, film: Azione | Dramma | Commedia, clientID:int) -> str:
        if film in self._film_list:
            if clientID in self._rented_film:
                self._rented_film[clientID].append(film)
            else:
                self._rented_film[clientID] = [film]
            self._film_list.remove(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")
    
    def giveBack(self, film:  Azione | Dramma | Commedia, clientID: int, days: int) -> str:
        self._rented_film[clientID].remove(film)
        self._film_list.append(film)
        penale: float = film.getPenale() * days
        print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} e' di {penale} euro!")

    def printMovies(self) -> list[Azione | Dramma | Commedia]:
        for i in self._film_list:
            print(f"{i.getTitle()} - {i.getGenere()}")

    def printRentMovies(self, clientID: int) -> str:
        print(self._rented_film[clientID])
        
    

    