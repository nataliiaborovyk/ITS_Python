'''
Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.
Suggerimento: ogni volta che si effettua una chiamata ricorsiva, 
si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri 
compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.
'''


def vowelsCounter(frase:str) -> str:

    if len(frase) == 0:
        return 0
    
    else:
        if frase[0].lower() in "aeiou":
            return 1 + vowelsCounter(frase[1:])
        else:
            return vowelsCounter(frase[1:])
    
print("\n", vowelsCounter("elefante"), "\n")




    