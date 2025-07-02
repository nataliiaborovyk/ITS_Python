'''
Esercizio 6 – Uso con reduce()
Usa reduce() (dal modulo functools) e una lambda per calcolare il prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].
'''

from functools import reduce

numeri = [2, 3, 4]
prodotto = reduce(lambda x,y: x*y, numeri)
print(prodotto)
