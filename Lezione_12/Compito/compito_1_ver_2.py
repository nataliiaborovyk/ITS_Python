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
        self.stato = True

    def setTitolo(self, titolo:str):
        self.titolo = titolo

    def setAutore(self, autore:str):
        self.autore = autore

    def setStato(self, stato:str):
        self.stato = stato

    def getTitolo(self):
        return self.titolo
    
    def getAutore(self):
        return self.autore
    
    def getStato(self):
        return self.stato


    
class Biblioteca:
    def __init__(self):
        self.libri:list[Libro] = []

    def aggiungi_libro(self, libro:Libro):
        self.libri.append(libro)
        print(f"Libro {libro.getTitolo()} di {libro.getAutore()} è stato aggiunto in Biblioteca")

    def presta_libro(self, titolo:str):

        for k in self.libri:
            if k.getTitolo() == titolo:
                if k.getStato() == True:
                    print(f"\nLibro {k.getTitolo()} è disponibile per il prestito")
                    k.setStato(False)
                    return
                else:
                    print(f"\nPurtroppo il libro {k.getTitolo()} per il momento è in prestito")
                    return
            
        print(f"\nBiblioteca non ha libro {titolo}")          
          
            
    def restituisci_libro(self, titolo):

        for k in self.libri:
            if k.getTitolo() == titolo:
                if k.getStato() == False:
                    print(f"\nLibro {k.getTitolo()} è restituito correttamente e adesso è disponibile")
                    k.setStato(True)
                    return
                else:
                    print(f"\nLibro {k.getTitolo()} non era stato prestato")
                    return
        print(f"\nErrore! Non puoi restituire libro {titolo} perche non è di questa biblioteca")

    def mostra_libri_disponibili(self):
        
        if not self.libri:
            print("\nPer il momento non ci sono libri disponibili")
        else: 
            print("\nLa Biblioteca ha seguenti libri: ")
            libri_ordinati:list[Libro] = sorted(self.libri, key=lambda k: k.getTitolo().lower())    #vorrei che stampa i libri in ordine alfabetivo
            for k in libri_ordinati:
                stato:str = "Disponibile" if k.getStato() else "Prestato"
                print(f"Titolo: {k.getTitolo()}, Autore: {k.getAutore()}, Stato: {stato}")
            
     

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
    
    collezione_1.restituisci_libro("Cucina italiana")
    collezione_1.restituisci_libro("Cucina italiana")
    collezione_1.restituisci_libro("Gatti")

