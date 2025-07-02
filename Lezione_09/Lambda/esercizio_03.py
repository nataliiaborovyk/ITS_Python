'''
Esercizio 3 – Uso con filter()
Hai la seguente lista numeri = [5, 12, 17, 18, 24, 32]. Usa filter() con una lambda per ottenere solo i numeri pari.
'''


lista_numeri:list = [5, 12, 17, 18, 24, 32]

lista_pari:list = list(filter(lambda x: x % 2 == 0, lista_numeri))

print(lista_pari)