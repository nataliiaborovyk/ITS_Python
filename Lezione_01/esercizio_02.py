'''
2. Trova il massimo tra 4 numeri:
Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.
'''
'''
max = 0
for i in range(4):
    n: int = int(input("\nInserisci il numero: "))
    if n > max:
        max = n
print(f"\nIl numero max: {max}")

max = 0 
i = 1
while i <= 4:
    n: int = int(input("\nInserisci il numero: "))
    if n > max:
        max = n
    i += 1
print(f"\nIl numero max: {max}\n")
'''
# versione 2

max: int = 0
for i in range(4):
    n: int = int(input("\nInserisci il numero: "))
    if i == 0:
        max = n
    elif n > max:
        max = n
print(f"\nIl numero max: {max}\n")

#versione 3

max: int = 0 
i = 1
while i <= 4:
    n: int = int(input("\nInserisci il numero: "))
    if i == 1:
        max = n
    elif n > max:
        max = n
    i += 1
print(f"\nIl numero max: {max}\n")

#versione 4

max: int = 0 
i = 0
while True:
    if i < 4:
        n: int = int(input("\nInserisci il numero: "))
        if i == 0:
            max = n
        elif n > max:
            max = n
        i += 1
    else:
        break

print(f"\nIl numero max: {max}\n")