# Esercizio 8.A

class Frazione:
    
    # class attributes
    __num: int
    __den: int

    # inizializzare un oggetto della classe Frazione
    def __init__(self, n: int, d: int):
    
        self.setNum(n)
        self.setDen(d)

    # impostare il valore del numeratore
    def setNum(self, n: int) -> None:
        # verifica se n è un istanza di int o float e nel caso in cui sia float, usa la funzione is_integer() dei float, ovvero 
        # verifica che n sia un numero intero ma scritto come float (ovvero 3.0) 
        if isinstance(n, int) or (isinstance(n, float) and n.is_integer()): 
            self.__num = int(n)
        else:
            self.__num = 13
        
        # nota
        # x = 2,   x.is_integer() -> True
        # x = 2.0, x.is_integer() -> True
        # x = 3.5, x.is_integer() -> False

        # ma questo dipende dagli interpreti.
        # su alcuni interpreti x=2, x.is_integer() funziona e ritorna True, su altri 
        # può succedere che se x=2, x.is_integer() può generare un AttributeError

        # x = 2,   isistance(x, int) -> True
        # x = 2.0, isistance(x, int) -> False
        # x = 3.5, isistance(x, int) -> False
    
    # impostare il valore del denominatore
    def setDen(self, d: int) -> None:
        if d != 0 and (isinstance(d, int) or (isinstance(d, float) and d.is_integer())):
            
            self.__den = int(d)
        else:
            self.__den = 5
    
    # ritornare il valore del numeratore
    def gNum(self) -> int:
        return self.__num
    
    # ritornare il valore del denominatore
    def gDen(self) -> int:
        return self.__den
    
    # restituire il valore della frazione arrotondato a 3 cifre decimali
    def value(self) -> float:
        return round(self.gNum() / self.gDen(), 3)
    
    # visualizzare in output un oggetto della classe Frazione
    def __str__(self) -> str:
        return f"{self.gNum()} / {self.gDen()}"     


# Esercizio 8.B

def mcd(x: int, y: int) -> int:
    
    # se x e y non hanno divisori in comune, sicuramente avranno in comune 1 come massimo comun divisore, 
    # perchè tutti i numeri sono divisibili per 1.
    max_divisor = 1

    # con un unico ciclo, devo calcolare i divisori di x, i divisori di y e vedere quali sono i divisori che x e y hanno in comune.
    # Se ad esempio, x= 6 e y = 12, sicuramente i divisori che x=6 e y=12 hanno in comune saranno più piccoli o uguali a 6.
    # Dunque, non avrò divisori comuni che siano più grandi di x=6. 
    # Pertanto, posso prendere in considerazione il valore più piccolo tra x e y come valore di arresto del ciclo per il calcolo del mcd. 
    end: int = min(x, y)
    
    
    for i in range(end,1,-1):

        # l'indice i gioca il ruolo di divisore per i numeri x e y 

        # i divisori di x sono dati da:
        # x % i == 0

        # i divisori di y sono dati da 
        # y % i == 0

        # troviamo i divisori comuni, ovvero i valori di i per cui la divisione x/i da resto 0 e la divisione y/i da resto 0
        if x % i == 0 and y % i == 0:

            # una volta trovato i per cui ottengo un divisore comune per x e y, 
            # devo controllare se questo divisore in comune sia il più grade
            if i > max_divisor:
                max_divisor = i 
    
    return max_divisor

# versione più veloce che evita molte iterazioni:
'''
def mcd(x: int, y: int) -> int:
    
    # se x e y non hanno divisori in comune, sicuramente avranno in comune 1 come massimo comun divisore, 
    # perchè tutti i numeri sono divisibili per 1.
    max_divisor = 1

    # con un unico ciclo, devo calcolare i divisori di x, i divisori di y e vedere quali sono i divisori che x e y hanno in comune.
    # Se ad esempio, x= 6 e y = 12, sicuramente i divisori che x=6 e y=12 hanno in comune saranno più piccoli o uguali a 6.
    # Dunque, non avrò divisori comuni che siano più grandi di x=6. 
    # Pertanto, posso prendere in considerazione il valore più piccolo tra x e y come valore di arresto del ciclo per il calcolo del mcd. 
    end: int = min(x, y)
    
    # eseguo il ciclo a ritroso, ovvero parto dal valore più piccolo tra x e y, e ad ogni iterazione decremento di 1. 
    # appena trovo un divisore che è comune a x e y, interrompo il cilco e ritorno il divisore. 
    # il primo divisore in comune che ho trovato è il più grande, in quanto ho fatto il ciclo a ritroso.

    for i in range(end,0,-1):

        # l'indice i gioca il ruolo di divisore per i numeri x e y 

        # i divisori di x sono dati da:
        # x % i == 0

        # i divisori di y sono dati da 
        # y % i == 0

        # troviamo i divisori comuni, ovvero i valori di i per cui la divisione x/i da resto 0 e la divisione y/i da resto 0
        if x % i == 0 and y % i == 0:

            # una volta trovato i per cui ottengo un divisore comune per x e y, 
            # devo controllare se questo divisore in comune sia il più grade
            return i
'''


# Esercizio 8.C

def semplifica(l: list[Frazione]) -> list[Frazione]:
    # usiamo la funzione mcd avendo come parametri di input il numeratore e denominatore di ogni frazione per semplificare le frazioni della lista,
    # fino a quando il cmd avrà valore uguale a 1. 
    l_simplified: list[Frazione] = []

    for f in l:
        
        d: int = mcd(f.gNum(), f.gDen())

        # per ogni frazione della lista controlla se la frazione è gia irriducibile, ovvero se il suo mcd tra numeratore e denominatore è 1.
        if d == 1:
            # in caso affermativo, aggiungila alla lista l_simplified
            l_simplified.append(f)
        # se la frazione non è irriducibile, semplificala
        else:
            # per semplificare una frazione ai minimi termini, dividiamo sia il numeratore e che il denominatore per il loro mcd,
            # ovvero numeratore = numeratore / mcd(numeratore, denominatore)
            # e denomionatore = denominatore / mcd(numeratore, denominatore)
            # fino a che mcd(numeratore, denominatore) sia uguale a 1

            # creo una copia dell'oggetto frazione
            # ricordiamo che la divisione in python restiuisce un float, anche se il risultato della divisione è un numero intero (es. 3.0)
            
            f_s: Frazione = Frazione(f.gNum() / d, f.gDen() / d)

            
               
            # una volta semplificata la frazione, aggiungila alla lista l_simplified
            l_simplified.append(f_s)
    
    # ritorna la lista l_simplified con tutte le frazioni ridotte.
    return l_simplified

# Esercizio 8.D

def fractionCompare(l: list[Frazione], l_s: list[Frazione]) -> None:
    # le due liste hanno la stessa lunghezza
    for i in range(len(l)):
        print(f"Valore frazione originale: {l[i].value()} --- Valore frazione ridotta: {l_s[i].value()}")


# Esercizio 8.E

if __name__ == "__main__":


    l:list[Frazione] = [
        Frazione(2.5, 0),
        Frazione(1,2),
        Frazione(2,4),
        Frazione(3,5),
        Frazione(6,9),
        Frazione(4,7),
        Frazione(24,36),
        Frazione(12,36),
        Frazione(40,60),
        Frazione(5,11),
        Frazione(10,45),
        Frazione(42,78),
        Frazione(9,15)
    ]

    # stampare lista l
    print("Originale\n")
    print(*l, sep="  ,  ")
    # lista l con frazioni ridotte
    l_s: list[Frazione] = semplifica(l)
    print("\nSemplificata\n")
    print(*l_s, sep = "  ,  ")

    print("\n")
    fractionCompare(l, l_s)
    



