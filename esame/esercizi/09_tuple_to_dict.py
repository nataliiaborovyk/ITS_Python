'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
'''

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    diz: dict[str:list[int]] = {}
    for tupl in tuples:
        if tupl[0] not in diz:
            diz[str(tupl[0])] = [int(tupl[1])]
        else:
            diz[str(tupl[0])].append(int(tupl[1]))
    return diz