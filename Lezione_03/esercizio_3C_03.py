'''
Esercizio 3C-3. Creare in Python una lista vuota chiamata 'oggetti'. 
Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per 
classificare gli oggetti presenti nella lista:
- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"
'''

#Esercizio 3C-3
print("\n Esercizio 3C-3\n")

oggetti:list = []

for i in range(3):
    oggetti.append(input("Inserisci oggetto: "))
    #x:str = input("Inserisci oggetto: ")
    #oggetti.append(x)

print(f"\n La lista contiene: {oggetti}")

match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("\n Materiale scolastico \n")
    case ["pane", "latte", "uova"]:
        print("\n Prodotti alimentari \n ")
    case ["sedia", "tavolo", "armadio"]:
        print("\n Mobili \n")
    case ["telefono","computer", "tablet"]:
        print("\n Dispositivi elettronici \n")
    case _:
        print("\n Categoria sconosciuta \n")