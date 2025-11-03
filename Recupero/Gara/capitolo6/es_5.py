'''
Sala dell'Equilibrio
Segnala problema

Il consiglio classifica ogni reagente: corrosivo, inerte o tonico. 
Formula `sign(n)` così da restituire `-1` per negativi, `0` per zero e `1` per positivi. 
Mantieni la firma e promuovi i test.
'''

def sign(n: int) -> int:
    if n >0:
        return 1
    elif n==0:
        return 0
    else:
        return -1