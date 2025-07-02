'''
Esercizio 8 – Doppio ordinamento
Hai una lista di dizionari:
studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]
Ordina la lista in ordine decrescente di media usando una funzione lambda.
'''

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

lista_media:list = sorted(studenti, key = lambda x: x["media"]  )

print(lista_media)