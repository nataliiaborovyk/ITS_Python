'''
Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano 
(sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, 
espresso come numero intero e usare un match per determinare il corrispondente GPA americano, 
secondo questa tabella di conversione:
- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"
'''

#Esercizio 3C-2
print("\n Esercizio 3C-2 \n")

voto = int(input("Inserisci un voto di laurea italiano compreso tra 66 e 110: "))

match voto:
    case voto if voto >= 106 and voto <=110:
        print("Voto nel sistema GPA é 4.0\n")
    case voto if voto >= 101 and voto <=105:
        print("Voto nel sistema GPA é 3.7\n")
    case voto if voto >= 96 and voto <=100:
        print("Voto nel sistema GPA é 3.3\n")
    case voto if voto >=91 and voto <=95:
        print("Voto nel sistema GPA é 3.0\n")
    case voto if voto >= 86 and voto <=90:
        print("Voto nel sistema GPA é 2.7\n")
    case voto if voto >= 81 and voto <=85:
        print("Voto nel sistema GPA é 2.3\n")
    case voto if voto >= 76 and voto <=80:
        print("Voto nel sistema GPA é 2.0\n")
    case voto if voto >= 70 and voto <=75:
        print("Voto nel sistema GPA é 1.7\n")
    case voto if voto >= 66 and voto <=69:
        print("Voto nel sistema GPA é 1.0\n")
    case _:
        print("Voto non valido")
