'''
Futuri Possibili

Hai `n` reagenti puri: quante miscele teoriche esistono, 
considerando tutti i sottoinsiemi? 
Realizza `powerset_size(n)` e restituisci quel conteggio. 
Mantieni la firma e titola i test.
'''

def powerset_size(n: int) -> int:
    if type(n) is int and n >= 0:
        return 2**n