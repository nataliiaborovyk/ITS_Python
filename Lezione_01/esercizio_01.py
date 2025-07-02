'''
1. Calcolo cateto di un triangolo rettangolo:
Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo 
rettangolo, conoscendo quelle dell’ipotenusa a e dell’altro cateto b.
'''

ipotenusa: float = float(input("\nInserisci la ipotenusa:  "))
cateto_1: float = float(input("\nInserisci il cateto:  "))

if ipotenusa > cateto_1:
    cateto_2: float = (ipotenusa ** 2 - cateto_1 ** 2) ** 0.5
    print(f"\nAltro cateto è: {cateto_2:.2f}\n")
else:
    print("Error")
