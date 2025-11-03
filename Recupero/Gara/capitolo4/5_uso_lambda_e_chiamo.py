'''
Rimbalzo Arcano

Raffina la soluzione lasciando che il filtro agisca due volte: 
usa `apply_twice(fn, x)` applicando `fn` a `x` due volte di seguito 
e restituendo il risultato. 
Mantieni la firma e supera i test.
'''

def apply_twice(fn, x):
    f = lambda i: fn(fn(i))
    return f(x)