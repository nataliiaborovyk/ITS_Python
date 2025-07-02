'''
1. Sistema di gestione per un parcheggio
Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un parcheggio 
con un numero massimo di posti dato in input. L'utente può inserire una delle seguenti opzioni 
"ingresso", "uscita", "stato", "esci". Per ogni opzione:
    se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
    se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
    se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
    se l'utente inserisce "esci", termina l'algoritmo.
Torna all'inserimento di una opzione finché l'utente non seleziona "esci".
'''

posti: int = int(input("\nInserisci il numero di posti totali nel parcheggio: "))
liberi: int = posti
while True:
    opzione: str = input("I\nnserisci una delle seguenti opzioni \"ingresso\", \"uscita\", \"stato\", \"esci\":  ").lower()
    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi -= 1
            else:
                print("\nNON CI SONO I POSTI DISPONIBILI")
        case "uscita":
            if liberi < posti:
                liberi += 1
            else:
                print("\nTUTTI I POSTI SONO DISPONIBILI")    
        case "stato":
            print(f"Posti liberi: {liberi}")   
            print(f"Posti occupati: {posti - liberi}")
        case "esci":
            break
        case _:
            print("\nError, riinserisci opzione:")