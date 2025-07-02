'''
6. Calcolo del fattoriale di un numero
Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente.
'''

while True:
    n:int = int(input("Inserisci un numero intero: "))
    if n % 1 == 0 and n > 0:
        break
    print("Error")

fattoriale:int = 1
i = 1
while True:
    if i > n:
        print(fattoriale)
        break
    else:
        fattoriale *= i
        i += 1

for i in range(1,n+1):
    fattoriale *= i
print(fattoriale)