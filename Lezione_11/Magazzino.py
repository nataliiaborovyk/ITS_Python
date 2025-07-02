'''
Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.
Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
Test case:
    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.
'''

class Prodotto:

    def __init__(self, name:str = "", quantita:int = 0) -> None:
        self.name = name
        self.quantita = quantita

    def setName(self, name:str) -> None:
        self.name = name

    def setQuantita(self, quantita:int) -> None:
        if quantita > 0:
            self.quantita = quantita
        else: 
            print(f"Error, la quantita \"{quantita}\" deve essere maggiore di 0")

    def getName(self) -> str:
        return self.name
    
    def getQuantita(self) -> int:
        return self.quantita

    def __str__(self) -> str:
        return f"Prodotto: {self.name}, quantita: {self.quantita}"
    
    
class Magazzino:
    def __init__(self):
        self.elenco:dict[str, Prodotto] = {}

    def aggiungi_prodotto(self, prod: Prodotto):
        p_name:str = prod.getName().lower()
        if p_name in self.elenco:   
            self.elenco[p_name].quantita += prod.getQuantita()
            #self.elenco[p_name].quantita - atributo di class Prodotto
        else: 
            self.elenco[p_name] = prod
       
    def cerca_prodotto(self, name:str) -> Prodotto:
        if name.lower() in self.elenco:
            return self.elenco[name.lower()]
        else:
            return f"Prodotto {name} non esiste nel magazino"
        
    def verifica_disponibilita(self, name:str) -> str:
        if name.lower() in self.elenco:
            return f"Prodotto {self.elenco[name.lower()].getName()} è disponibile in magazzino in quantita di {self.elenco[name.lower()].getQuantita()} unita"
        else:
            return f"Prodotto {name} non è disponibile nel magazino"    
 
    def __str__(self) -> str:
        result: str = "Nel magazzino sono disponibili sequenti prodotti: \n"
        for k, v in self.elenco.items():
            result += f"{v.name}: {v.quantita}\n"
        return result



if __name__ == "__main__":

    print("\n      Class Prodotto")
    p1:Prodotto = Prodotto()
    print(p1)   
    p1 = Prodotto("latte", 3)
    print(p1)
    p2 = Prodotto("pane", 8)
    print(p2)
    p3 = Prodotto("pasta", 10)
    print(p3)

    print("\n      Class Magazzino")
    m1:Magazzino = Magazzino()
    m1.aggiungi_prodotto(p1)
    m1.aggiungi_prodotto(p2)
    m1.aggiungi_prodotto(p3)
    m1.aggiungi_prodotto(p1)
    print(m1)

    print("cerso prodotto latte", m1.cerca_prodotto("latte"))
    print("cerso prodotto LATTE", m1.cerca_prodotto("LATTE")) 
    print(m1.cerca_prodotto("PomoDORi"))

    print("verifico se \"pane\" c'è nel magazzino\n", m1.verifica_disponibilita("pane"))
    print("verifico se \"PANE c'è nel magazzino\n", m1.verifica_disponibilita("PANE"))
    print(m1.verifica_disponibilita("FARinA"))