'''
1-6. Inserire all'interno di un dizionario il menu' di un ristorante, 
che viene specificato alla fine della traccia di questo esercizio.
Aggiungere in un nuovo dizionario chiamato ordine, un primo, 
un secondo, un contorno, una bevanda ed un dolce preso dal menu'. 
Stampare a schermo il conto totale che il cliente dovrà pagare. 

ITS Bakery Menu':
Pizza: 9.00 euro
Pasta: 10.50 euro
Zuppa : 7.00 euro
Hamburger: 15.50 euro
Cotoletta: 10.00 euro
Salmone: 20.20 euro
Patatine Fritte: 5.50 euro
Patate al forno: 5.50 euro
Verdura del giorno: 7.00 euro
Cheesecake: 6.00 euro
Tiramisu': 6.00 euro
Focaccia con Nutella: 6.00 euro
Coca Cola: 3.50 euro
Acqua: 1.50 euro
Vino: 5.00 euro
'''



#esercizio_6
print("\n   Esercizio 6\n")
menu:dict = {
"Pizza":9.00, 
"Pasta":10.50,
"Zuppa":7.00,
"Hamburger":15.50,
"Cotoletta":10.00,
"Salmone":20.20,
"Patatine fritte":5.50,
"Patate al forno":5.50,
"Verdura del giorno":7.00,
"Cheesecake":6.00,
"Tiramisu":6.00,
"Focaccia cin Nutella":6.00,
"Coca Cola":3.50,
"Acqua":1.50,
"Vino":5.00}

ordine:dict = {
"Zuppa":7.00,
"Salmone":20.20,
"Verdure del giorno":7.00,
"Tiramisu":6.00,
"Acqua":1.50}

print("  Menu contiene:")
for k,v in menu.items():
   print(k,v)

print("\n  Ordine del cliente")
for k, v in ordine.items():
    print(f"Piatto: {k} Prezzo: {v} Euro")

print("\nversione 1")
da_pagare:float = 0
da_pagare = da_pagare + ordine["Zuppa"]
da_pagare += ordine["Salmone"]
da_pagare += ordine["Verdure del giorno"]
da_pagare += ordine["Tiramisu"]
da_pagare += ordine["Acqua"]
print(f"\nTotale da pagare è {da_pagare}") 

print("\nversione 2")
somma:float = 0
for i in ordine.values():
    somma += i
print(f"\nTotale da pagare è {somma}\n")
 


 

