'''
Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli 
  e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. 
Il libro deve essere inizialmente disponibile (non prestato).
- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi della classe:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. 
      Restituisce un messaggio di stato.
    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. 
      Restituisce un messaggio di stato.
    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
      Se non ci sono libri disponibili, restituisce un messaggio di errore.

Codice Driver
    Aggiungi libri alla biblioteca.
    Presta e restituisci libri, gestendo anche casi limite (già prestato, doppia restituzione, libro inesistente).
    Mostra i libri disponibili in ogni fase.
    Visualizza lo stato finale di ogni libro.
'''


class Libro:

    def __init__(self):
        self.titolo = ""
        self.autore = ""
        self.stato = "Disponibile"

    def setTitolo(self, titolo:str):
        self.titolo = titolo

    def setAutore(self, autore:str):
        self.autore = autore

    def setStatoPrestito(self, stato:str):
        self.stato = stato

    def getTitolo(self):
        return self.titolo
    
    def getAutore(self):
        return self.autore
    
    def getStatoPrestito(self):
        return self.stato


    
class Biblioteca:
    def __init__(self):
        self.libriDisponibili:list[Libro] = []
        self.libriPrestati:list[Libro] = []

    def aggiungi_libro(self, libro:Libro):
        self.libriDisponibili.append(libro)
        print(f"Libro {libro.getTitolo()} di {libro.getAutore()} è stato aggiunto in Biblioteca")

    def presta_libro(self, titolo:str):

        for i in self.libriDisponibili:
            if i.getTitolo() == titolo:
                print(f"\nLibro {i.getTitolo()} è disponibile per il prestito")
                self.libriPrestati.append(i)
                self.libriDisponibili.remove(i)
                return
        

        for i in self.libriPrestati:
            if i.getTitolo() == titolo:
                print(f"\nPurtroppo il libro {i.getTitolo()} per il momento è in prestito")
                return
            
        print(f"\nBiblioteca non ha libro {titolo}")          
          
            
    def restituisci_libro(self, titolo):

        for i in self.libriPrestati:
            if i.getTitolo() == titolo:
                print(f"\nLibro {i.getTitolo()} è restituito e adesso è disponibile")
                self.libriPrestati.remove(i)
                self.libriDisponibili.append(i)
                return
        print(f"\nErrore! Non puoi restituire libro {titolo} perche non è di questa biblioteca")

    def mostra_libri_disponibili(self):
        
        if not self.libriDisponibili:
            print("Per il momento non ci sono libri disponibili")
        else: 
            print("\nLa Biblioteca ha seguenti libri disponibili per prestito: ")
            libri_ordinati_disp:list[Libro] = sorted(self.libri.Disponibili, key=lambda i: i.getTitolo().lowe())   #stampa in ordine alfabetivo
            for i in libri_ordinati_disp:
                print(f"Titolo: {i.getTitolo()}, Autore: {i.getAutore()}")
            
        if self.libriPrestati:
            print("\nLa Biblioteca ha anche seguenti libri ma per il momento sono in prestito: ")
            libri_ordinati_prest:list[Libro] = sorted(self.libriPrestati, key=lambda i: i.getTitolo().lower())
            for i in self.libriPrestati:
                print(f"Titolo: {i.getTitolo()} Autore: {i.getAutore()}")       

if __name__ == "__main__":


    libro_1:Libro =Libro()
    libro_1.setTitolo("Cucina italiana")
    libro_1.setAutore("Marco Rossi")

    libro_2:Libro = Libro()
    libro_2.setTitolo("Piccolo Principe")
    libro_2.setAutore("Antoine de Saint-Exupéry")

    fm:Libro = Libro()
    fm.setTitolo("Avventure")
    fm.setAutore("Federico")

    collezione_1:Biblioteca = Biblioteca()
    collezione_1.aggiungi_libro(libro_1)
    collezione_1.aggiungi_libro(libro_2)
    collezione_1.aggiungi_libro(fm)

    collezione_1.mostra_libri_disponibili()

    collezione_1.presta_libro("Avventure")
    collezione_1.mostra_libri_disponibili()
    
    collezione_1.presta_libro("Cucina italiana")
    collezione_1.mostra_libri_disponibili()
    
    collezione_1.presta_libro("Gatti")

    collezione_1.restituisci_libro("Avventure")
    collezione_1.restituisci_libro("Gatti")
    collezione_1.restituisci_libro("Cucina italiana")
    collezione_1.restituisci_libro("Cucina italiana")
