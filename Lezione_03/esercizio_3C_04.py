'''
Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire 
il nome di un animale e, utilizzando un match statement, identifichi a quale categoria 
esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:
- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.
Se l'animale non appartiene a nessuna delle categorie sopra elencate,  mostrare un messaggio 
indicante che il programma non è in grado di classificare l'animale inserito.
Suggerimento: Utilizzare una lista per ognuna della quattro categorie.
'''

#Esercizio 3C-4
print("\n Esercizio 3C-4\n")

nome:str = input("Digita il nome di un animale: ")

mammiferi:list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili:list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list[str] = ["aquila", "pappagallo", "gufo", "falco"]
pesci:list[str] = ["squallo", "trota", "salmone", "carpa"]

match nome:
    case nome if nome in mammiferi:
        print(f"{nome} appartiene alla categoria dei Mammiferi")
    case nome if nome in rettili:
        print(f"{nome} appartiene alla categoria dei Rettili")
    case nome if nome in uccelli:
        print(f"{nome} appartiene alla categoria dei Uccelli")
    case nome if nome in pesci:
        print(f"{nome} appartiene alla categoria dei Pescic")
    case _:
        print("Il programma non è in grado di classificare l'animale inserito")