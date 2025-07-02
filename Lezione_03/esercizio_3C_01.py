''' 
Esercizio 3C-1. Scrivere un programma in Python che utilizzi un match statement 
per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e 
stampare la valutazione corrispondente:
- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"
'''

#Esercizio 3C-1
print("\nEsercizio 3C-1\n")

voto: int = int(input("Inserisci il voto numerico intero da 1 a 10: \n"))

match voto:
    case 10:
        print("Eccellente\n")
    case 8|9:
        print("Molto buono\n")
    case 6|7:
        print("Sufficiente\n")
    case 4|5:
        print("Insufficiente\n")
    case 1|2|3:
        print("Gravemente insufficiente\n")
    case _:
        print("Voto non valido\n")
