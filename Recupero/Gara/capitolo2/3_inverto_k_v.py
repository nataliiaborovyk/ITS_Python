'''
Alleanze Invertite

Per evitare errori, inverti gli indici della tabella: 
ogni valore rimandi all'essenza originaria. 
Usa `invert_unique(d)` che inverte chiavi e valori assumendo valori univoci. 
Mantieni la firma e passa i test.
'''

def invert_unique(d: dict) -> dict:
    diz:dict = {}
    for k, v in d.items():
        diz[v] = k

    return diz

# alternativi
def invert_unique(d: dict) -> dict:
    return {v: k for k, v in d.items()}
