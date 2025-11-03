'''
Fontana di Mercurio

Nei canalicoli del reattore evita divisioni impossibili. 
Usa `safe_div(a, b, default=None)`: se `b` vale `0`, restituisci `default`; 
altrimenti il risultato in **virgola mobile**. Mantieni la firma e promuovi i test.
'''

def safe_div(a: float, b: float, default=None):
    if b == 0:
        return default
    else:
        return a/b