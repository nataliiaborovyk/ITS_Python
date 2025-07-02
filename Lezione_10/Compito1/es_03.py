'''
Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 
L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro 
e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.
For example:
Test 	Result
print(calcola_stipendio(40))   400.0
print(calcola_stipendio(0))     0.0
'''



def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        return ore_lavorate * 10
    else: 
        return (ore_lavorate - 40) * 15 + 40 * 10
    
print(calcola_stipendio(40))   
print(calcola_stipendio(0))