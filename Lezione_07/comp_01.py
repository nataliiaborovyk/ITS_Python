'''

Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.

For example:
Test 	Result

print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))    {1: 'a', 2: 'b', 3: 'c'}
print(inverti_mappa({}))   {}
print(inverti_mappa({'a': 3, 'b': 3, 'c': 3}))  {3: 'a'}     
print(inverti_mappa({'a': 1, 'b': 1, 'c': 2}))     {1: 'a', 2: 'c'}    
print(inverti_mappa({'a': 2, 'b': 1, 'c': 2}))   {2: 'a', 1: 'b'}
'''

def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:
    dizionario_invertito:dict[int:str] = {}
    for k, v in dizionario.items():
        if v in dizionario_invertito:
            continue
        else:
            dizionario_invertito[v] = k
    return dizionario_invertito

print(inverti_mappa({'a': 1, 'b': 2, 'c': 3})) 
print(inverti_mappa({'a': 3, 'b': 3, 'c': 3}))