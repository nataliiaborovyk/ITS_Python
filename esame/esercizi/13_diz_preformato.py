'''
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
'''
def classifica_numeri(lista: list[int]) -> dict[str:list[int]]:
    diz:dict[str:list[int]] = {'pari':[], 'dispari':[]}
    for n in lista:
        if n % 2 == 0:
            if n not in diz['pari']:
                diz['pari'].append(n)
        else:
            if n not in diz['dispari']:
                diz['dispari'].append(n)
    return diz