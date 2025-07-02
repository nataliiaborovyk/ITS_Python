

class Media:

    _title: str
    _reviews: list[int]


    def __init__(self, title:str) -> None:
        self.set_title(title)
        self._reviews = []

    def set_title(self, title:str) -> None:
        self._title = title

    def get_title(self) -> str:
        return self._title
    
    def aggiungiValutazione(self, voto:int) -> None:
        if type(voto) == int and (1 <= voto <= 5):
            self._reviews.append(voto)
        
    def getMedia(self) -> float:
        if len(self._reviews) == 0:
            raise ValueError("Non ci sono le recensioni")
        len_reviews: int = len(self._reviews)
        somma: int = sum(self._reviews)
        media: float = somma / len_reviews
        return media

    def getRate(self) -> str:
        if self.getMedia() < 1.4:
            return "Terribile"
        if self.getMedia() < 2.4:
            return "Brutto"
        if self.getMedia() < 3.4:
            return "Normale"
        if self.getMedia() < 4.4:
            return "Bello"
        if self.getMedia() >= 1.4:
            return "Grandioso"
        
    def ratePercentage(self, voto:int) -> float: 
        cont = 0
        for i in self._reviews:
            if i == voto:
                cont += 1
        percentuale: float = cont/len(self._reviews)*100
        return round(percentuale, 2)
    
    def recensione(self) -> str:
        print(f"\nTitolo del Film: {self.get_title()} \nVoto Medio: {self.getMedia()}" 
              + f"\nGiudizio: {self.getRate()}% \nTerribile: {self.ratePercentage(1)}%"
              + f"\nBrutto: {self.ratePercentage(2)}% \nNormale: {self.ratePercentage(3)}%"
              + f"\nBello: {self.ratePercentage(4)}% \nGrandioso: {self.ratePercentage(5)}%")
        

class Film(Media):
    def __init__(self, title) -> None:
        super().__init__(title)

if __name__ == "__main__":
    f1: Film = Film("Kill Bill")
    f1.aggiungiValutazione(5)
    print(f1.getMedia())
    f1.recensione()
    f1.aggiungiValutazione(4)
    f1.aggiungiValutazione(4)
    f1.aggiungiValutazione(2)
    f1.recensione()
        
