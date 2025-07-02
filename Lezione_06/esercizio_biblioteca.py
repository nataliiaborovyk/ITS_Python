class Libro:

    def __init__(self):
        self.titolo:str = ""
        self.autore:str = ""
        self.genere:list[str] = []
        
    def setAutore(self, autore:str):
        self.autore = autore

    def setTitolo(self, titolo:str):
        self.titolo = titolo

    def setGenere(self, lista_genere:list):
        self.genere = lista_genere

    def getAutore(self) -> str:
        return self.autore
    
    def getTitolo(self) -> str:
        return self.titolo
    
    def getGenere(self) -> list[str]:
        return self.genere
    

class Biblioteca:
    def __init__(self):
        self.libri:list[Libro] = []

    def setLibro(self, libro:Libro):
        self.libri.append(libro)

    def getLibriTitolo(self) -> str:
        for i in self.libri:
            
            print(f"Titolo: {i.getTitolo()}\nAutore: {i.getAutore()}\nGenere: {i.getGenere()}\n")
        


if __name__ == "__main__":

    libro_1:Libro = Libro()

    libro_1.setTitolo("Piccolo Principe")
    libro_1.setAutore("Antoine de Saint-Exupéry")
    libro_1.setGenere(["Narrativa"])

    fm:Libro = Libro()

    fm.setTitolo("Aventure")
    fm.setAutore("Federico")
    fm.setGenere(["Comico"])

    collez_1:Biblioteca = Biblioteca()

    collez_1.setLibro(libro_1)
    collez_1.setLibro(fm)

    collez_1.getLibriTitolo()

    print("-------------------")

    test:Libro = Libro()
    test.setTitolo("Harry Potter")
    test.setAutore("Rowling")
    test.setGenere(["Fantasy"])

    collez_1.setLibro(test)

    collez_1.getLibriTitolo()