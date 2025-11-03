'''
Melodia Compressa

Per documentare una reazione registra serie di simboli compressi: 
usa `rle(s)` costruendo una lista di `(carattere, conteggio)` 
per gruppi consecutivi; se `s` è vuota, `[]`. 
Mantieni la firma e titola i test.
'''

def rle(s: str) -> list[tuple[str,int]]:
    if not s:
        return []
    sc: str = s[:]
    lista:list = []
    cont = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cont += 1
        else:
            lista.append((s[i-1], cont))
            cont = 1
    lista.append((s[-1], cont))
    return lista
