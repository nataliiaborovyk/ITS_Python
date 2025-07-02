'''
2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
'''

def cort(lista:list[int]) -> dict:
    diz:dict[list[int]] = {"numeri positivi":[], "numeri negativi":[]}
    for i in lista:
        if i >= 0:
            diz["numeri positivi"].append(i)
        else:
            diz["numeri negativi"].append(i)
    return diz

print(cort([1,-3,5,-5]))