'''
7. Conta i numeri pari e dispari
Progetta un algoritmo che dati 10 numeri forniti dall'utente, 
conta quanti sono pari e quanti dispari.
'''

pari:int = 0
dispari: int = 0
cont:int = 0
while True:
    if cont == 10:
        print(pari)
        print(dispari)
        break
    else:
        n:int = int(input("Inserisci un numero intero: "))
        if n % 2 == 0:
            pari += 1
        else:
            dispari += 1
        cont += 1

for cont in range(11):
    if cont == 10:
        print(pari)
        print(dispari)
        break
    else:
        n:int = int(input("Inserisci un numero intero: "))
        if n % 2 == 0:
            pari += 1
        else:
            dispari += 1
        cont += 1

for cont in range(10):
    n:int = int(input("Inserisci un numero intero: "))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1
print(pari)
print(dispari)