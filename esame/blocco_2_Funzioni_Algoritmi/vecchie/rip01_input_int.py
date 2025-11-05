'''
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

def num_int(frase:str):
    while True:
        n: str = input(frase)
        try:
            x:float = float(n)
            if x.is_integer() and x >= 0:
                return int(x)
            else:
                print('Inserisci il numero positivo')
        except ValueError:
            print('inserisci il numero valido')

    
def num_seg(fun):
    def wrapper():
        print('Inserisci 0 per terminare')
        return fun()
    return wrapper

@num_seg
def sequenza():
    lista:list[int] = []
    while True:
        y:int = num_int("Inserisci il numero positivo: ")
        if y == 0:
            break
        else:
            lista.append(y)
    return lista

def func():
    x:int = num_int('inserisci il numero preferito: ')
    seg:list[int] = sequenza()
    print("Sequenza inserita:", seg)
    occor: int = 0
    index:int = None
    somma: int = 0
    for i in seg:
        if i == x:
            if not index:
                index = seg.index(i)
            occor += 1
        else:
            somma += i
    
    if not index:
        print(f"il numero {x} non comparre nella s00eguenza")
    elif occor == 1:
        print(f"il numero {x} comparre {occor} volta nella seguenza")
    else:
        print(f"il numero {x} comparre {occor} volte nella seguenza")
    print(f"Il numero {x} compare per la prima volta in posizione {index} nella sequenza")
    print(f"La somma dei valori della sequenza diversi da {x} e' {somma}")
    
    



func()

