
'''
Trama Lineare

A fine procedura versa tutto nello stesso crogiolo creando un flusso uniforme. 
Ottienilo con `flatten_once(nested)`, che concatena le sottoliste a un solo livello. 
Mantieni la firma e fai riuscire i test.
'''

def flatten_once(nested: list[list[int]]) -> list[int]:
    lista_nuova:list = []
    for i in range(len(nested)):
        for k in range(len(nested[i])):
            lista_nuova.append(nested[i][k])
    return lista_nuova


# alternativi

def flatten_once(nested: list[list[int]]) -> list[int]:
    lista_nuova: list[int] = []
    for i in nested:
        for k in i:
            lista_nuova.append(k)
    return lista_nuova

def flatten_once(nested: list[list[int]]) -> list[int]:
    return [x for sub in nested for x in sub]
