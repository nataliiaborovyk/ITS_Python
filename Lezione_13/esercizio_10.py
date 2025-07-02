'''
Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa 
e restituisca il risultato sotto forma di una nuova stringa.
Ad esempio, se la stringa "libro" viene data in input a charDuplicator, 
la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".
'''

def charDuplicator(frase:str) -> str:
    if len(frase) == 0:
        return ""
    else:
        return frase[0]*2 + charDuplicator(frase[1:])
    
print("\n", charDuplicator("elefante"), "\n")