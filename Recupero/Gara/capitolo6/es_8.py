'''
Specchi Paralleli
Segnala problema

Contieni la temperatura del crogiolo tra soglia bassa e alta. 
Implementa `clamp(x, lo, hi)` restituendo il valore limitato a `[lo, hi]`.
 Mantieni la firma e titola i test.
'''

def clamp(x: float, lo: float, hi: float) -> float:
    if x > hi:
        return hi
    elif x < lo:
        return lo
    else:
        return x