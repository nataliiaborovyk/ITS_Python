'''
1. Verifica se una stringa è un numero intero
Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti.
Esempio:
is_integer("123")      # True
is_integer("-456")     # True
is_integer("12.3")     # False
'''
import re

def is_integer(s:str) -> bool:
    
    match = re.fullmatch(r'-?\d+', s)
    if match:
        print(True)
    else:
        print(False)

is_integer("645")
is_integer("64")
is_integer("-456") 
is_integer("12.3") 