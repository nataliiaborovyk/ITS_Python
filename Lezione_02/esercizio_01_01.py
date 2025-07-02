'''
1-1. Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:

    Memorizzare un numero in virgola mobile nella variabile x.
    Calcolare 1.0/x memorizzare il risultato nella variabile y.
    Visualizzare il valore di x, y e il prodotto tra x e y.
    Sottrarre x dal prodotto tra x e y e mostrarne il risultato.
'''

#esercizio_1
print("    Esercizio 1\n ")

x:float = 2.57
y:float = 1.0 / x
prod:float = x * y
dif:float = prod - x

print(f"x = {x}")
print(f"y = {y}")
print(f"x * y = {prod}")
print(f"(x * y) - x = {dif}")