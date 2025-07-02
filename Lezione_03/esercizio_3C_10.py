'''
Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data
 (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match 
 statement per verificare se la data corrisponde a una festività o a un evento speciale:
- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."
'''

#Esercizio 3C-6
print("\n Esercizio 3C-6\n")

print("Inserisci una data (giorno e mese espressi in forma numerica)")

giorno:int = int(input("\nInserisci il giorno: "))
mese:int = int(input("\nInserisci il mese: "))

data:tuple = (giorno, mese)

match data:
    case (1,1):
        print(f"\nIl {giorno}/{mese} è Capodanno")
    case (14,2):
        print(f"\nIl {giorno}/{mese} è San Valentino")
    case (2,6):
        print(f"\nIl {giorno}/{mese} è Festa della Repubblica Italiana")
    case (15,8):
        print(f"\nIl {giorno}/{mese} è Ferragosto")
    case (31, 10):
        print(f"\nIl {giorno}/{mese} è Halloween")
    case (25, 12):
        print(f"\nIl {giorno}/{mese} è Natale")
    case _:
        print(f"\nNessuna festivita importante in questa data {giorno}/{mese}\n")

        
