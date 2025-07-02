'''
9. Classifica delle vendite
Progetta un algoritmo che forniti dall'utente 20 totali di vendita 
e i nomi dei venditori, trova i due nomi dei venditori 
con il totale più alto e il totale più basso delle vendite.
'''

#nome: str = input("Inserisci il nome del venditore: ")
#vendita: float = float(input("Inserisci il valore di vendita: "))

#max_nome = nome
#max = vendita
#min_nome = nome
#min = vendita

'''
cont = 0

while True:
    if cont == 3:
        print(f"Venditore {max_nome} ha venduto il massimo {max},il venditore {min_nome} ha venduto il {min}")
        break
    else:
        new_nome: str = input("Inserisci il nome del venditore: ")
        new_vendita: float = float(input("Inserisci il valore di vendita: "))
        if cont == 0:
            max = new_vendita
            max_nome = new_nome
            min = new_vendita
            min_nome = new_nome
        if new_vendita > max:
            max_nome = new_nome
            max = new_vendita
        else:
            if new_vendita < min:
                min_nome = new_nome
                min = new_vendita
        cont += 1
    
'''

for cont in range(1, 22):
    if cont == 21:
        print(f"Venditore {max_nome} ha venduto il massimo {max},il venditore {min_nome} ha venduto il {min}")
        break
    else:
        nome: str = input("Inserisci il nome del venditore: ")
        vendita: float = float(input("Inserisci il valore di vendita: "))
        if cont == 1:
            max = vendita
            max_nome = nome
            min = vendita
            min_nome = nome
        if vendita > max:
            max_nome = nome
            max = vendita
        else:
            if vendita < min:
                min_nome = nome
                min = vendita
        
    