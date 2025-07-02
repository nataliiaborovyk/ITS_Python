'''
Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python 
che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 
classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre 
a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale 
inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".
Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.
Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; 
dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.
Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.
Categorie di habitat: acqua, aria, terra
NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.
'''

#Esercizio 3C-6
print("\n Esercizio 3C-6\n")

# input dei dati

nome:str = input("\nDigita il nome di un animale: ").lower()
habitat:str = input("\nDigita l'habitat in cui vive l'animale: ").lower()
#habitat_2:str = input("\nDigita un altro l'habitat in cui vive l'animale (se non esiste digita solo \"Enter\"):  ").title()

lista_mammiferi:list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]
lista_rettili:list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
lista_uccelli:list[str] = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
lista_pesci:list[str] = ["squallo", "trota", "salmone", "carpa"]
#lista_habitat:list[str] = [acqua, aria, terra]

# assegno la categoria giusta all'animale inserito

animal_type:str = ""
 
match nome:
    case nome if nome in lista_mammiferi:
        animal_type = "Mammiferi"
        print(f"\n{nome.title()} appartiene alla categoria dei {animal_type}\n")
        
    case nome if nome in lista_rettili:
        animal_type = "Rettili"
        print(f"\n{nome.title()} appartiene alla categoria dei {animal_type}\n")
        
    case nome if nome in lista_uccelli:
        animal_type = "Uccelli"
        print(f"\n{nome.title()} appartiene alla categoria dei {animal_type}\n")
       
    case nome if nome in lista_pesci:
        animal_type = "Pesci"
        print(f"\n{nome.title()} appartiene alla categoria dei {animal_type}\n")
    case _:
        animal_type = "Unknown"
        print(f"\nCategoria sconosciuta: {animal_type}\n")

# inserisco i dati nel dizionario
diz:dict = {}
diz["Nome"] = nome
diz["Categoria"] = animal_type
diz["Habitat"] = habitat

#stampo il dizionario
for k, v in diz.items():     
    print(f"{k}: {v}")

# Liste dei habitat in quali possono vivere l'animali
acqua:list = ["serpente", "tartaruga", "coccodrillo", "anatra", "cigno", "squallo", "trota", "salmone", "carpa"]
aria:list = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra"]
terra:list = ["cane", "gatto", "cavallo", "elefante", "leone", "serpente", "lucertola", "tartaruga", "coccodrillo", "gallina", "tacchino"]

#verifico in quali altri habitat puo vivere animale da input

match diz:

    case diz if diz["Categoria"] == "Unknown":
        print(f"\nNon so dire in quale categoria classificare l'animale {nome}! ")
        print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}")

    case diz if diz["Habitat"] == "acqua":
        if nome in acqua:
            print(f"\nAnimale {nome} vive solo nell'acqua") 
        elif nome in aria:
            print(f"\nAnimale {nome} vive nell'acqua e nell'aria")
        elif nome in terra:
            print(f"\nAnimale {nome} vive nell'acqua e sulla terra")

    case diz if diz["Habitat"] == "aria":
        if nome in aria:
            print(f"\nAnimale {nome} vive nell'aria") 
        elif nome in acqua:
            print(f"\nAnimale {nome} vive nell'aria e nell'acqua")
        elif nome in terra:
            print(f"\nAnimale {nome} vive nell'aria e sulla terra")   

    case diz if diz["Habitat"] == "terra":
        if nome in terra:
            print(f"\nAnimale {nome} vive solo sulla terra") 
        elif nome in aria:
            print(f"\nAnimale {nome} vive sulla terra e nell'aria")
        elif nome in acqua:
            print(f"\nAnimale {nome} vive sulla terra e nell'aria")
    
   

match diz:

    case diz if diz["Categoria"] == "Unknown":
        print(f"\nNon so dire in quale categoria classificare l'animale {nome}! ")
        print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}")

    case diz if diz["Habitat"] == "acqua":
        match nome:
            case nome if nome in acqua:
                print(f"\nAnimale {nome} vive solo nell'acqua") 
            case nome if nome in aria:
                print(f"\nAnimale {nome} vive nell'acqua e nell'aria")
            case nome if nome in terra:
                print(f"\nAnimale {nome} vive nell'acqua e sulla terra")

    case diz if diz["Habitat"] == "aria":
        match nome:
            case nome if nome in aria:
                print(f"\nAnimale {nome} vive nell'aria") 
            case nome if nome in acqua:
                print(f"\nAnimale {nome} vive nell'aria e nell'acqua")
            case nome if nome in terra:
                print(f"\nAnimale {nome} vive nell'aria e sulla terra")   

    case diz if diz["Habitat"] == "terra":
        match nome:
            case nome if nome in terra:
                print(f"\nAnimale {nome} vive solo sulla terra") 
            case nome if nome in aria:
                print(f"\nAnimale {nome} vive sulla terra e nell'aria")
            case nome if nome in acqua:
                print(f"\nAnimale {nome} vive sulla terra e nell'aria")
    








  
'''
# versione 2
print("\n\tVersione 2 senza usare i dizionari")

match nome:
    case nome if nome in aria and nome in acqua and nome in terra:
        print(f"Animale {nome} vive in aria, acqua e terra")
    case nome if nome in acqua and nome in aria:
        print(f"Animale {nome} vive nell'aria e nell'acqua")
    case nome if nome in terra and nome in aria:
        print(f"Animale {nome} vive sulla terra e nell'aria")
    case nome if nome in acqua and nome in terra:
        print(f"Animale {nome} vive nell'acqua e sulla terra")
    case nome if nome in acqua:
        print(f"Animale {nome} vive solo nell'acqua")
    case nome if nome in aria:
        print(f"Animale {nome} vive solo nell'aria")
    case nome if nome in terra:
        print(f"Animale {nome} vive solo sulla terra")
    case _:
        print(f"\nNon so dire in quale categoria classificare l'animale {nome}! ")
        print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}")
    
'''
 

'''

match diz:
    case {"Nome": name,  "Categoria": anymal_tipe,  "Habitat_1": "Acqua"|"",  "Habitat_2": ""|"Acqua"}:
        print(f"\nAnimale {name.title()} appartiene alla categoria dei {animal_type} e puo vivere solo in acqua\n")

    case {"Nome": name,  "Categoria": anymal_tipe,  "Habitat_1": "Acqua"|"Terra",  "Habitat_2": "Terra"|"Acqua"}:
        print(f"\nAnimale {name.title()} appartiene alla categoria dei {animal_type} e puo vivere nell'acqua e sulla terra \n")

    case {"Nome": name,  "Categoria": anymal_tipe,  "Habitat_1": "Terra"|"",  "Habitat_2": ""|"Terra"}:
        print(f"\nAnimale {name.title()} appartiene alla categoria dei {animal_type} e puo vivere solo sulla terra\n")

    case {"Nome": name,  "Categoria": anymal_tipe,  "Habitat_1": "Aria"|"Terra",  "Habitat_2": "Terra"|"Aria"}:
        print(f"\nAnimale {name.title()} appartiene alla categoria dei {animal_type} e puo vivere nell'aria e sulla terra \n")

    case {"Nome": name,  "Categoria": anymal_tipe,  "Habitat_1": "Aria"|"",  "Habitat_2": ""|"Aria"}:
        print(f"\nAnimale {name.title()} appartiene alla categoria dei {animal_type} e puo vivere solo nel aria\n")

    case {"Nome": name,  "Categoria": anymal_tipe,  "Habitat_1": "Aria"|"Acqua",  "Habitat_2": "Acqua"|"Aria"}:
        print(f"\nAnimale {name.title()} appartiene alla categoria dei {animal_type} e puo vivere solo sulla terra\n")
    
    case _:
        print(f"Non so dire in quale categoria classificare l'animale e in quale habitat vive")
'''       