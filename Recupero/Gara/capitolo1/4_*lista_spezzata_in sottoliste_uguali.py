'''
Segmenti Rituali

Per stabilizzare il rituale travasa i reagenti in fiale di volume costante. 
Usa `chunk(lst, size)` per ottenere sottoliste di lunghezza `size` (l'ultima può variare). 
Mantieni la firma e supera i test come una titolazione regolare.
'''

def chunk(lst: list[int], size: int) -> list[list[int]]:
    lista_nuova: list = []
    div: int = len(lst) // size
    resto: int = len(lst) % size
    indice = 0
    for i in range(div):
        lista:list = []
        while len(lista) < size:
            lista.append(lst[indice])
            indice += 1
        lista_nuova.append(lista)
    if resto > 0:
        lista: list = []
        lista = lst[div*size:].copy()
        lista_nuova.append(lista)
    return lista_nuova

print(chunk([1,2,3,4,5,6,7,8,9,10], 4))

# alternative

def chunk(lst: list[int], size: int) -> list[list[int]]:
    # Scelta: se size <= 0, sollevo un errore (coerente con "volume costante")
    if size <= 0:
        raise ValueError("size deve essere > 0")
    out: list[list[int]] = []
    # range(0, len(lst), size) crea gli starting index dei blocchi
    for i in range(0, len(lst), size):
        out.append(lst[i:i + size])  # l'ultimo può essere più corto
    return out


def chunk(lst: list[int], size: int) -> list[list[int]]:
    if size <= 0:
        raise ValueError("size deve essere > 0")
    return [lst[i:i + size] for i in range(0, len(lst), size)]
