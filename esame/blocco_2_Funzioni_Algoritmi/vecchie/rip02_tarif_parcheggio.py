'''
Esercizio 1.
 
Un garage fa pagare una tariffa minima di 2.00 $ per parcheggiare fino a tre ore, più 0.50 $ all'ora per ogni ora o parte di essa oltre le tre ore. Il costo per un periodo di 24 ore di parcheggio ammonta a 10.00 $. Supponete che nessuna macchina resti parcheggiata per più di 24 ore.
Elaborare un algoritmo che calcoli e stampi i costi del parcheggio per una dato periodo di tempo.
 
Una volta elaborato l'algoritmo, scrivere in Python, una funzione calculateCharges() che consenta di determinare il costo del parcheggio per un dato cliente.
 
Scrivere un codice Python che consenta di calcolare i costi del parcheggio per ciascuno dei quattro clienti che ieri hanno parcheggiato le loro auto in questo garage. Mostra, poi, i risultati in forma tabellare.
Il vostro output deve avere il seguente formato:

Car         Hours          Charge
 1             1.5               2.00 $
 2             4.0              2.50 $
 3             5.50            3.50 $
 4             24.0            10.00 $        
 TOTAL    35.0            18.00 $
 
 

'''

def calculateCharges(diz:dict[str, float]):
    print(f"{'Car':<10}{'Hours':<15}{'Pay':<10}")
    ore_tot = 0
    paga_tot = 0
    for car,ore in diz.items():
        ore_tot += ore
        if ore % 24 == 0:
            paga = 10.00
        elif ore <= 3:
            paga = ore* 2.00
        else:
            paga = (ore - 3) * 0.5 + 3 * 2
        paga_tot += paga
        print(f"{car:<10}{ore:<15}{paga:<15}")
        
    print(f"{"Total":<10}{ore_tot:<15}{paga_tot:<10}")

g1 = {1:5,2:3,3:19,4:24}

calculateCharges(g1)