'''
Esercizio 3C-00B. Scrivere un programma in Python che chieda all'utente di inserire 
il proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) e utilizzi 
lo statement match per fornire una risposta adeguata da inserire in un documento di identita'.
- Se il valore di gender è "m", stampare il nome e il genere come Maschio.
- Se il valore di gender è "f", stampare il nome e il genere come Femmina.
- Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, 
indicando che non è possibile generare un documento di identità.
'''

#Esercizio 3C-00B
print("\nEsercizio 3C-00B\n")

nome:str = input(f"Inserisci il proprio nome: \n")
gen:str = input(f"Inserisci il suo genere (ez. \"m\" o \"f\"): \n")

match (nome, gen):
    case (x, "m"):
        print(f"Nome: {x}, gerene: \"Maschio\"\n")
    case (y, "f"):
        print(f"Nome: {y}: genere \"Femmina\"\n")
    case _:
        print(f"\"Errore\" non è possibile generare un documento di identita\n")