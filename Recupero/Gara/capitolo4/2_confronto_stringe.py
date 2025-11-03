'''
Parole Gemelle

Due etichette di fiale, mischiate, potrebbero descrivere lo stesso composto. 
Confermalo con `are_anagrams(a, b)` ignorando spazi e maiuscole. 
Torna `True` se coincidono nelle lettere, altrimenti `False`. 
Mantieni la firma e chiarisci i test.
'''

def are_anagrams(a: str, b: str) -> bool:
    a1 = a.replace(" ", "").lower()
    b1 = b.replace(" ", "").lower()
    if len(a1) != len(b1):
        return False
    a2 = sorted(a1)
    b2 = sorted(b1)
    if a2 == b2:
        return True
    return False
