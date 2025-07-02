'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

For example:
Test 	Result

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))    [1, 3, 4]

print(rimuovi_elementi([], {2: 1}))   []
'''
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for k,v in da_rimuovere.items():
        for i in lista:
            if i == k:
                if v >= 1:
                    lista.remove(i)
                    v -= 1
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))    

print(rimuovi_elementi([], {2: 1}))   

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))