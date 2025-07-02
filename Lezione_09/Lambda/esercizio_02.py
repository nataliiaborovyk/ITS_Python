'''
Esercizio 2 – Somma di due numeri
Crea una funzione lambda che accetti due numeri e restituisca la loro somma.
'''

from typing import Callable

somma:Callable[[int,int], int] = lambda x, y: x + y

print(somma(5,7)) 