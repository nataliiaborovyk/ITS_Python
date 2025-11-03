'''
Esercizio 1.
 

8.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente numeratore e denominatore.
Si definiscano i metodi __init__, setter, getter, __str__, value.
In particolare:

    il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;

    il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
    i metodi setter devono controllare che il valore inserito sia un intero, in caso contrario il numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5. Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.

Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer() e isistance().


8.B Il Massimo Comun Divisore di due o più numeri è il più grande divisore comune dei numeri considerati.
Ad esempio, se consideriamo i numeri 12 e 18, il loro Massimo Comun Divisore è mcd(12,18) = 6.
Infatti,

    i divisori di 12 sono:

        12 = 1, 2, 3, 4, 6, 12

    i divisori di 18 sono:

        18 = 1, 2, 3, 6, 9, 18

il divisore più grande che 12 e 18 hanno in comune è 6.

Scrivere nel file frazione.py una funzione  mcd(int x, int y) per il calcolo del Massimo Comune Divisore.
 
Nel caso in cui esista un Massimo Comun Divisore tra i numeri x e y, allora la funzione deve ritornarlo come numero intero.
Altrimenti, nel caso in cui non esista un massimo Comun Divisore tra i numeri x e y, la funzione deve ritornare 1.
   

Suggerimento: per semplicità, per implementare la funzione richiesta, trovare una soluzione che generalizzi l'esempio proposto e che tenga conto dei casi x > y e x < y per evitare di replicare righe di codice.
   
8.C Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni, ovvero il più grande divisore comune tra numeratore e denominatore è 1.

Sia l una lista di frazioni, ovvero una lista di oggetti della classe Frazione.

Si scriva nel file frazioni.py una funzione chiamata semplifica() che data in input una lista di frazioni ritorni in output una lista di frazioni irriducibili.
 
Nello specifico:

    se una frazione f della lista data in input è già irriducibile, allora inserire questa frazione f nella lista da ritornare in output.

 

    se una frazione f della lista data in input può essere semplificata, in una frazione irriducibile f1, allora si deve prima semplicare la frazione f, ottenendo la frazione irriducibile f1 e poi inserire f1 nella lista da ritornare in output.


Suggerimento: Leggere bene la traccia dell'intero esercizio per capire come implementare la funzione semplifica.
Inserire in modo adeguato le seguenti frazioni nella lista l.
   
8.D Scrivere in Python una funzione chiamata fractionCompare() che prende in input la lista di frazioni l originale e la lista con le frazioni di l semplificata.
 
Usando il metodo value(), dimostrare che il valore di ogni funzione di entrambe le liste non cambia, stampandolo in output.
Esempio:

    Valore frazione originale: 0.538 --- Valore frazione ridotta: 0.538
   

8.E Scrivere un codice Python che inizializzi la seguente lista l di frazioni, dove ogni frazione è un oggetto della classe Frazione:
 
l = 2.5/0,   1/2,   2/4,   3/5,   6/9,   4/7,   24/36,   12/36,   40/60,   5/11,   10/45,   42/78,   9/15
       
Sfruttando la funzione semplifica, generare una nuova lista chiamata l_s, contente una versione semplificata delle frazioni della lista l.
Infine, richiamando la funzione fractionCompare, dimostrare che le funzioni delle lista l e l_s sono equivalenti, ovvero hanno lo stesso valore.
 
Esercizio 2.
 
Scrivere un programma Python che legge in input prima un intero x positivo e poi una sequenza di interi positivi. Se l'utente inserisce il numero 0, allora la sequenza deve terminare.

Per il numero x e per ogni numero della sequenza inserita, effettuare il controllo che il numero inserito sia effettivamente un intero e forzare l'utente ad inserire un numero intero positivo nel caso in cui questa condizione non venga rispettata.
Trovare una soluzione che eviti di scrivere codice duplicato per effettuare questa serie di controlli.
 
Suggerimento: per controllare che un numeri sia intero, usare la funzione is_integer() e isistance().

Determinato il numero x e la sequenza di interi positivi, il programma deve produrre in output:
 

    stampare la sequenza
#
    Il numero occ di occorrenze di x, ovvero  il numero di volte in cui appare x nella sequenza;

    La posizione pos del primo valore uguale a x.

    La somma di tutti i valori diversi da x;


Ad esempio, se l'utente inserisce come valore x il numero 3 e poi immette la sequenza: 7; 5; 1; 3; 3; 3; 11; 2; 3; 3; 0
 
il programma dovra' scrivere in output:

    stampare in output la sequenza

    Il numero 3 compare 5 volte nella sequenza (attenzione all'output se il numero compare 1 sola volta!)

    Il numero 3 compare per la prima volta in posizione 3 nella sequenza

    La somma dei valori della sequenza diversi da 3 e' 26


'''


# es 1 8A

class Frazione:

    __numeratore:int
    __denuminatore:int

    def __init__(self, numeratore: int, denominatore: int) -> None:
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def set_numeratore(self, numeratore:int) -> None:
        #if type(numeratore) != int:
        if isinstance(numeratore, int):
            self.__num = numeratore
        elif isinstance(numeratore, float) and numeratore.is_integer():
            self.__num = int(numeratore)
        else:
            self.__num = 13

    def set_denominatore(self, denominatore:int) -> None:
        if type(denominatore) != int or denominatore == 0:
            self.__denom = 5
        else:
            self.__denom = denominatore

    def get_numeratore(self) -> int:
        return self.__num
    
    def get_donominatore(self) -> int:
        return self.__denom

    def value(self) -> float:
        if self.__denom == 0:
            raise ValueError('denominatore non puo essere 0')
        return round(self.__num / self.__denom, 3)
    
    def __str__(self) -> str:
        return f"{self.__num} / {self.__denom} = {self.value()}"
    

# 8 B


def mcd(x: int, y:int):

    x = abs(x)
    y = abs(y)

    if x == 0 and y == 0:
        return 1 
    if x == 0:
        return y
    if y == 0:
        return x

    div_x:set = set()
    for n in range(1,x+1):
        if x % n == 0:
            div_x.add(n)

    div_y:set = set()
    for n in range(1, y+1):
        if y % n == 0:
            div_y.add(n)

    div_comune:set = div_x & div_y

    if div_comune:
        return max(div_comune)
    else:
        return 1
    
    
    
        
