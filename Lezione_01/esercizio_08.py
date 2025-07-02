'''
8. Trovare i numeri maggiori di un valore soglia
Progetta un algoritmo che dati 7 numeri, 
trova e comunica i numeri maggiori di un valore soglia fornito dall'utente.
'''

soglia:int = int(input("Inserisci una soglia: "))
cont:int = 0
while True:
    if cont == 7:
        break
    else:
        n:int = int(input("Inserisci un numero intero: "))
        if n > soglia:
            print(f"Numero {n} è maggiore di {soglia}")
    cont += 1


