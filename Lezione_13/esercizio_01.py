'''
Scrivere in Python una funzione recursivePower che calcola la potenza di un numero utilizzando la ricorsione. 
La funzione deve ricevere due parametri in input:
    base: il numero da elevare a potenza.
    exponent: l’esponente a cui elevare la base.
'''

def recursivePower(base:int, exp:int) -> int:
    if exp == 0:
        return 1
    else:
        return base * recursivePower(base, exp-1)
    
print("\n", recursivePower(3,4), "\n")      #perche c'è spazio prima del risultato in output?
print(recursivePower(4,3), "\n")
print(recursivePower(2,5), "\n")
print(recursivePower(5,2), "\n")