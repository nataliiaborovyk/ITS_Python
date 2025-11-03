'''

Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio.

'''

class Contatore:

    def __init__(self) -> None:
        self.contatore = 0

    def setZero(self) -> None:
        self.contatore = 0

    def add1(self) -> None:
        self.contatore += 1

    def sub1(self) -> None:
        if self.contatore <= 0:
            print("Non è possibile eseguire la sottrazione")
        else: 
            self.contatore -= 1
            if self.contatore <= 0:
                self.contatore = 0

    def get(self) -> int:
        return self.contatore
    
    def mostra(self) -> str:
        print(f"Conteggio attuale: {self.contatore}")
        


    