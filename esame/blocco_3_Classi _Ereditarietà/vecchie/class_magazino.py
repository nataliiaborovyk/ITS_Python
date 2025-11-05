'''
            es 2 Gestione di un magazzino

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

    def __init__(self, nome:str, quantita:int) -> None:
        self.nome = nome
        self.quantita = quantita

    def get_nome(self) -> str:
        return self.nome
    
    def quantita_disp(self) -> int:
        return self.quantita
    

class Magazzino:
     
    def __init__(self, elenco:list[Prodotto] = None) -> None:
        self.elenco = elenco or []

    def aggiungi_prod(self, prodotto:Prodotto) -> None:
        if prodotto in self.elenco:
            raise ValueError('il prodotto gia presente')
        self.elenco.append(prodotto)
     
    def cerca_prodotto(self, nome) -> Prodotto | str:
        for p in self.elenco:
            if p.get_nome() == nome:
                return p
        return f'non esiste {nome} nel magazino'
    
    def verifica_disponibilita(self, nome:str) -> str:
        prod = self.cerca_prodotto(nome)
        if isinstance(prod, Prodotto):
            if prod.quantita_disp() > 0:
                return f'prodotto {nome} - disponibile {prod.quantita_disp()}'
            return f'prodotto {nome}  è finito nel magazino'
        return f'prodotto {nome} non esiste nel magazino'
    
if __name__ == "__main__":

    p1=Prodotto('latte',5)
    p2=Prodotto('pane', 0)

    m=Magazzino()
    m.aggiungi_prod(p1)
    m.aggiungi_prod(p2)

    print(m.verifica_disponibilita('pane'))
    print(m.verifica_disponibilita('latte'))
    print(m.verifica_disponibilita('sale'))

    print(m.cerca_prodotto('uova'))