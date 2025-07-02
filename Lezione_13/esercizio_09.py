'''
Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data 
e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.
Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe 
al fine di costruire la stringa da restituire.
'''

def vowelRemover(frase:str) -> str:

    if len(frase) == 0:
        return ""
    else:
        if frase[0].lower() in "aeiou":
            return "" + vowelRemover(frase[1:])
        else:
            return frase[0] + vowelRemover(frase[1:])
        
print("\n", vowelRemover("elefante"), "\n")
