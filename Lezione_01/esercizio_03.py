'''
3. Calcolo della somma di numeri positivi
Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori 
inseriti dall'utente. Quindi, se un numero è negativo o zero, ignora quel valore nella somma.
'''

sum: int = 0
cont:int = 0

while True:
    n: int = int(input("\nInserisci il numero: "))

    if n > 0:    #solo se il numero inserito è positivo va sommato
        sum += n

    cont += 1
    
    if cont == 5:   #serve per uscire dal ciclo se utente ha gia inserito 5 valori
        break

print(f"\nLa somma dei soli numeri positivi è: {sum}\n")

    