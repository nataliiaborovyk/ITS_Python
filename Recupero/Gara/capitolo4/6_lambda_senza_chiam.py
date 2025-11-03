'''
Canale Intrecciato
Segnala problema

Nel reattore il primo reagente attiva il successivo: realizza `compose(f, g)`
 perché la funzione restituita calcoli prima `g(x)` e poi `f(...)`. 
Mantieni la firma e titola i test alla perfezione.
'''

def compose(f, g):
    return lambda x: f(g(x))