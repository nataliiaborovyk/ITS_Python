'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

For example:
Test 	Result

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))      {'a': [1, 3], 'b': [2]}

print(lista_a_dizionario([]))   {}
'''


    
def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    dizionario:dict = {}
    for k, v in tuples:
        if k in dizionario:
            dizionario[k].append(v)
        else:
            dizionario[k] = [v]
    return dizionario
