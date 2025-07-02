'''
1-3. Si scriva un programma che legge tre numeri interi 
e visualizza la media dei tre numeri.
'''


#esercizio_3
print("\n   Esercizio 3 versione 1\n")

x:int = int(input("inserisci il numero per calcolare la media  "))
y:int = int(input("inserisci il numero per calcolare la media  "))
z:int = int(input("inserisci il numero per calcolare la media  "))

media:float = (x + y + z)/3
print(f"Media di 3 numeri inseriti è {media:.1f}")



print("\n   Esercizio 3 versione 2\n")

somma:float = 0
quantita_numeri:int = 3

for i in range(quantita_numeri):
    x:int = int(input("inserisci il numero per calcolare la media  "))
    somma += x
    
media:float = somma / quantita_numeri
print(f"Media di {quantita_numeri} numeri inseriti è {media:.1f}")

