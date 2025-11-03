# inizializzare due numeri
n1:int = int(input("Digitare un numero: "))
n2:int = int(input("Digitare un secondo numero: "))

product:int = 1

# caso in cui n1 > n2
if n1 > n2:
    # calcolare il prodotto di tutti i numeri compresi tra n1 e n2, estremi inclusi
    for i in range(n2, n1+1):
        # aggiornare prodotto
        product *= i

# caso in cui n1 < n2
elif n1 < n2 :
    # calcolare il prodotto di tutti i numeri compresi tra n2 e n1, estremi inclusi
    for i in range(n1, n2+1):
        product *= i
        
# caso in cui n1 = n2
else :
    # il prodotto è uguale al numero inserito
    product = n1

# mostra in output il risultato
print(f"Prodotto: {product}")
