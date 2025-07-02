import math

def calculateCharges(h: float) -> float:
    # tariffa iniziale per le prime 3 ore
    if h <= 3:
        return 2.00
    # dalle 4 ore alle 23 
    # se ho ad esempio 4.5 ore paghero' 2.50 euro, perchè i 0,50 euro vengono aggiunti allo scattare della quinta ora. 
    elif h > 3 and h < 24:
        return (2.00 + ( (math.ceil(h)-3) * 0.5))
    # 24 ore 
    else:
        return 10.00



# mostrare i risultati in forma tabellare
# lista per salvare le ore di parcheggio di ciascun cliente
clients: list[float] = [1.5, 4.0, 5.5, 24.0]

# somma di tutte le tariffe
total_charges: float = 0.00

# prima riga
print(f"{'Car':<10}{'Hours':<10}{'Charges':<10}")

# seconda, terza e quarta riga
for i in range(4):
    # calcola tariffa per cliente
    cC: float = calculateCharges(clients[i])
    print(f"{i+1:<10}{clients[i]:<10}{cC:.2f} $")
    # calcola la somma di tutte le tariffe
    total_charges = total_charges + cC

# quinta riga
print(f"{'TOTAL':<10}{sum(clients):<10}{total_charges:<.2f} $")

# se voglio stampare qualcosa in output allineandolo a sinistra e facendo in modo che tutta la stampa occupi 10 posizioni farò
# : -> indica una formattazione
# < -> allinea a sinistra
# 10 -> la larghezza totale dell'output sarà di 10 caratteri

# total_charges[i]:<10.2f -> formatta il valore con due cifre decimali e fai in modo che l'output in totale occupi  10 caratteri. 


