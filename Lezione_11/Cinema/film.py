
class Film:
    
    def __init__(self) -> None:
        self.titolo: str = ""
        self.durata: int = 0

    def setTitolo(self, titolo: str) -> None:
        self.titolo = titolo

    def setDurata(self, durata: int) -> None:
        if durata < 0:
            raise ValueError("La durata deve essere > 0")
        self.durata = durata

    def getTitolo(self) -> str:
        return self.titolo   

    def getDurata(self) -> int:
        return self.durata 

    def __str__(self) -> str:
        return f"Film: \"{self.titolo}\" dura {self.durata} minuti"
    

