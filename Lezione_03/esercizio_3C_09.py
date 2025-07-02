'''
Esercizio 3C-9. Scrivere un programma in Python che permetta all'utente di inserire le coordinate 
di un punto (x, y) e salvi le coordinate inserite in una tupla. Utilizzare il  match statement 
per determinare la sua posizione del punto inserito nel piano cartesiano:
- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."
'''

#Esercizio 3C-6
print("\n Esercizio 3C-6\n")

print("Inserisci le coordinate di un punto(x,y)")

x:int = int(input("\nInserisci la coordinata X: "))
y:int = int(input("\nInserisci la coordinata Y: "))

punto:True = (x, y)

match punto:
    case (0, 0):
        print(f"\nIl punto (0, 0) si trova nell'origine")
    case (a, 0):
        print(f"\nIl punto ({a}, 0) si trova sull'asse X ")
    case (0, b):
        print(f"\nIl punto ({b}, 0) si trova sull'asse y ")
    case (x, y) if x > 0 and y > 0:
        print(f"\nIl punto ({x}, {y}) si trova nel primo quadrante")
    case (x, y) if x < 0 and y > 0:
        print(f"\nIl punto ({x}, {y}) si trova nel secondo quadrante")    
    case (x, y) if x < 0 and y < 0:
        print(f"\nIl punto ({x}, {y}) si trova nel terzo quadrante")
    case (x, y) if x > 0 and y < 0:
        print(f"\nIl punto ({x}, {y}) si trova nel quarto quadrante")