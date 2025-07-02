# Esercizi di recupero per il corso di Data Analyst 
# 04/07/2025 



# 1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
#    la chiave è già presente, somma il valore al valore già associato alla chiave.


from typing import Union


def convert_list_of_tuple_to_dict(list_1: list[tuple]) -> dict:
    
    dict_1: dict = {}
    
    for element in list_1:
        
        key, value = element[0], element[1]
        
        if key in dict_1:
            
            dict_1[key] += value
            
        else:

            dict_1[key] = value
            
    return dict_1



lista_1: list[tuple] = [(0, "valore1"), (1, "valore2")]
dict_2: dict = convert_list_of_tuple_to_dict(list_1=lista_1)


print(dict_2)

# 2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
#    classifichi i numeri in liste separate per numeri positivi e negativi.



def filter_positive_negative(list_1: list) -> dict:
    
    dict_1 = {"positivi": [], "negativi": []}


    for element in list_1:
        
        if element >= 0:
            
            if "positivi" not in dict_1:
                
                dict_1["positivi"] = []
            
            dict_1["positivi"].append(element)
            
        else:
            
         
            
            dict_1["negativi"].append(element)
            
    return dict_1


lista_3: list = [-2, 1, 4, 3, -7, 5, -9]

dict_3: dict = filter_positive_negative(list_1=lista_3)

print(f"La soluzione dell'esercizio 2 è: {dict_3}")


# 3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
#    restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
#    con i prezzi aumentati del 10% e arrotondati a due cifre decimali.


dict_5: dict = {"Penna": 1.5, "Samsung A55": 280.5, "Dell G16": 1450.6}


def filter_product_dict(dict_1: dict) -> dict:
    
    
    dict_4: dict = {}
    
    for key, value in dict_1.items():
        
        if value > 50:
            
            continue
        
        else:
            
            dict_4[key] = round(value + value * 0.10, 2)
    
    
    return dict_4


dict_out: dict = filter_product_dict(dict_1=dict_5)
print(f"La soluzione dell'esercizio 3 è: {dict_out}")



# 2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
#    dato valore intero definito threshold.

def product(lista_interi: list[Union[int, float]], soglia: int = 50) -> int:

    prodotto_cumulato: int = 1

    for element in lista_interi:
        
        if type(element) != int:
            
            continue
        
        if element < soglia:
            
            prodotto_cumulato *= element
            
    
    return prodotto_cumulato


# 2 bis) Calcola il fattoriale di un numero n

def factorial(n: int) -> int:
    
    fattoriale: int = 1
    
    for i in range(n):
        
        fattoriale *= n - i
        
    return fattoriale


def factorial(n: int) -> int:
    
    
    if n == 1:
        
        return n
    
    return factorial(n-1) * n


# 3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
#    a) 2, 4, 6, 8, 10, 12, 14
#    b) 1, 4, 7, 10, 13
#    c) 30, 25, 20, 15, 10, 5, 0
#    d) 5, 15, 25, 35, 45



for i in range(2, 15, 2):
    
    print(i)
    
    
for i in range(1, 14, 3):
    
    print(i)


lista = []
for i in range(30, -1, -5):
    lista.append(i)
    
print(*lista)

for i in range(5, 50, 10):
    
    print(i)