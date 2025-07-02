'''
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave
'''

def convert(lista:list[tuple]):
    diz: dict = {}
    for i,k  in lista:
        if i in diz:
            diz[i] += k
        else:
            diz[i] = k
    return diz

def conv(lista: list[tuple]):
    diz:dict = {}
    for i in lista:
        if i[0] in diz:
            diz[i[0]] += i[1]
        else:
            diz[i[0]] = i[1]
    return diz

print(conv([("a",1), ("b",2), ("a",3)]))
        
        
