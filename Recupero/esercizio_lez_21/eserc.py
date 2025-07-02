
class Documento:
    _testo: str

    def __init__(self, testo:str | None) -> None:
        self.set_testo(testo)

    def set_testo(self, testo:str) -> None:
        self._testo = testo

    def getText(self) -> str:
        return self._testo
    
    def isInText(self, parola:str) -> bool:
        if parola in self._testo:
            return True
        else:
            return False
        
    
class Email(Documento):
    _mittente: str
    _destinatario: str
    _titolo_messaggio: str


    def __init__(self, mittente:str, destinatario:str, titolo_messaggio:str, corpo_messaggio:str) -> None:
        self.set_titolo(titolo_messaggio)
        self.set_mittente(mittente)
        self.set_destinatario(destinatario)
        super().__init__(corpo_messaggio)

    def set_titolo(self, titolo_messaggio:str) -> None:
        self._titolo_messaggio = titolo_messaggio

    def set_mittente(self, mittente:str) -> None:
        self._mittente = mittente

    def set_destinatario(self, destinatario:str) -> None:
        self._destinatario = destinatario

    def get_titolo(self) -> str:
        return self._titolo_messaggio

    def get_mittente(self) -> str:
        return self._mittente
    
    def get_destinatario(self) -> str:
        return self._destinatario
    
    def getText(self) -> str:
        return f"Mittente: {self.get_mittente()}, Destinatario: {self.get_destinatario()}, \
            \nTitolo del messaggio: {self.get_titolo()}, Messagio: {super().getText()} "
    
    def writeToFile(self, PATH):
        with open(PATH, "w") as pippo:
            pippo.write(self.getText())  #scrittura al interno del file ma w sovrascrive il contenuto del file, a per aggiungere nel contenuto


class File(Documento):
    _nomePercorso: str

    def __init__(self, nomePercorso:str) -> None:
        self._nomePercorso = nomePercorso
    
    def leggiTestoDaFile(self):
        with open(self._nomePercorso, "r") as pippo:
            return pippo.read() #read tutto il file come str, readline(1) ritorna una riga, readlines ritorna una lista dove ogli elemento è una riga
    
test: Email = Email("fdkgshdg", "hgfs", "Titolo", "Mio messaggio")
test.writeToFile("./documento.txt")

topolino:File = File("./documento.txt")
print(topolino.leggiTestoDaFile())