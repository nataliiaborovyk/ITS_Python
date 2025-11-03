'''
## ### **B3.I.1 — Library Items (base OOP + override)**
**Task.**
Progettare una gerarchia di classi per gestire gli oggetti di una biblioteca.
Ogni oggetto (libro, DVD, ecc.) può essere preso in prestito e restituito.
Serve anche un metodo per descrivere i dati dell’oggetto.
---
### **Classe LibraryItem**
**Attributi:**
* `item_id: str` — identificativo univoco dell’oggetto.
* `title: str` — titolo dell’opera.
* `available: bool = True` — indica se l’oggetto è disponibile al prestito.
**Metodi:**
* `describe() -> str`: restituisce una stringa con ID, titolo 
e stato (“disponibile” o “non disponibile”).
* `borrow() -> bool`: se l’oggetto è disponibile, 
imposta `available=False` e restituisce `True`;
  altrimenti restituisce `False` senza modificare lo stato.
* `return_item() -> None`: imposta `available=True` (oggetto restituito).
---
### **Classe Book(LibraryItem)**
**Attributi aggiuntivi:**
* `author: str` — nome dell’autore.
**Metodi:**
* `describe() -> str`: **override** del metodo base.
  Restituisce una descrizione più completa, includendo l’autore.
### **Classe Dvd(LibraryItem)**
**Attributi aggiuntivi:**
* `duration_min: int` — durata in minuti.
**Metodi:**
* `describe() -> str`: **override** del metodo base, include anche la durata.
'''

class LibraryItem:
    def __init__(self, item_id: str, title: str) -> None:
        self.item_id: str = item_id
        self.title: str = title
        self.available: bool = True  # per chiarezza tipologica

    def describe(self) -> str:
        stato = "Disponibile" if self.available else "Non disponibile"
        return f"id: {self.item_id} | titolo: {self.title} | {stato}"

    def borrow(self) -> bool:
        if self.available:
            self.available = False
            return True
        return False

    def return_item(self) -> None:
        self.available = True


class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str) -> None:
        super().__init__(item_id, title)  # inizializza la classe base prima
        self.author: str = author

    def describe(self) -> str:
        stato = "Disponibile" if self.available else "Non disponibile"
        return f"id: {self.item_id} | titolo: {self.title} | autore: {self.author} | {stato}"


class Dvd(LibraryItem):
    def __init__(self, item_id: str, title: str, duration_min: int) -> None:
        super().__init__(item_id, title)
        self.duration_min: int = duration_min  

    def describe(self) -> str:
        stato = "Disponibile" if self.available else "Non disponibile"
        return f"id: {self.item_id} | titolo: {self.title} | durata: {self.duration_min} min | {stato}"
