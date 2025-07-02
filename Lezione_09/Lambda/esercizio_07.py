'''
Esercizio 7 – Filtra parole corte
Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"] 
Estrai solo le parole con più di 4 lettere usando filter() e lambda.
'''
import re
parole = ["cane", "gatto", "elefante", "ratto", "orso"] 
list_result:list = list(filter(lambda x: re.fullmatch(r"[a-zA-Z]{5,}", x), parole))
print(list_result)