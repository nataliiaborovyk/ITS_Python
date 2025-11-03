'''
Atlante Fuso

Due ricettari si sovrappongono: fondili lasciando prevalere le dosi più aggiornate. 
Implementa `merge_overwrite(a, b)` creando 
un nuovo dizionario con i valori di `b` che sovrascrivono `a`. 
Mantieni la firma e promuovi i test.
'''

def merge_overwrite(a: dict, b: dict) -> dict:
    diz: dict = a | b
    return diz

# c = a | b  uguale  c = a.copy()  c.update(b)

# u = a | b | c   prima a con b,    poi il risultato con c

# a |= b  aggiunge ad "a" le chiavi distinti di b e aggiorna quelli uguali con valori di b