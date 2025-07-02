'''
Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto. 
Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto 
dopo t mesi data una somma di partenza m.
'''
# VERSIONE 1

def compoundInterest(m:float, t:int) -> float:
    if t < 1:
        return round(m, 2)
    else:
        return round(1.005 * compoundInterest(m,t-1), 2)
    
print("\n",compoundInterest(10,3))


# VERSIONE 2

def compoundInterest_2(m:float, t:int) -> float:
    if t < 1:
        return m
    else:
        return 1.005 * compoundInterest_2(m,t-1)
    
print("\n",compoundInterest_2(10,3))


# VERSIONE 3

def compoundInterest_3(m:float, t:int) -> float:
    if t < 1:
        return m
    else:
        return compoundInterest_3(m*1.005,t-1)
    
print("\n",compoundInterest_3(10,3))