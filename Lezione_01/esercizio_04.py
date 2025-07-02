'''
4. Controllo della parità di un numero
Progetta un algoritmo utile a determinare se un numero 
inserito dall'utente è pari o dispari.
'''

n: int = int(input("\nInserisci un numero: "))
if n % 2 == 0:
    print(f"Il numero {n} è pari")
else:
    print(f"Il numero {n} è dispari")