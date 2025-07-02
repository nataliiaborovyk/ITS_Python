from film import Film



class Sala:
    
    def __init__(self) ->None:
        self.numId: int = 0
        self.filmAttuale: Film = None
        self.postiTot: int = 0
        self.postiPrenotati:int = 0
 
    def setNumId(self, numId: int) -> None:
        if numId > 0:
            self.numId = numId
        else:
            print(f"Error, Non si puo assegnare {numId} come numero identificatico della sala, il numero deve eseere maggiore di 0")

    def getNumId(self):
        return self.numId

    def setFilmAttuale(self, film: Film) -> None:
        self.filmAttuale = film

    def getFilmAttuale(self):
        return self.filmAttuale

    def setPostiTot(self, numPostTot:int) -> None:
        self.postiTot = numPostTot

    def prenota_posti(self, num_posti: int) -> str:
        if num_posti <= 0:
            return f"Error, numero dei posti {num_posti} non valido"
        
        if self.posti_disponibili() - num_posti < 0:
            result: bool = False
            return f"Stato di prenotazione: {result}.   Nella Sala {self.numId} purtroppo non ci sono {num_posti} liberi per il film {self.filmAttuale.getTitolo()} ma solo {self.posti_disponibili()}"           
        
        self.postiPrenotati += num_posti
        result: bool = True
        return f"Stato di prenotazione: {result}.   Hai prenotato {num_posti} posti"

    def posti_disponibili(self) -> int:
        return self.postiTot - self.postiPrenotati
    
    def __str__(self) -> str:
        if self.filmAttuale:
            return f"Sala: {self.numId}, Film attuale: \"{self.filmAttuale}\", numero posti disponibili: {self.posti_disponibili()} "
        return "Nessun film in programmazione"
