

def costo_parcheggio(ore) -> float:
    tariffa1:int = 2
    aumento:float = 0.5
    costo:float = 0
    if ore <= 3:
        costo = 2
    if ore > 3 and ore < 24:
        costo = (ore - 3) * 0.5 + 2
    if ore == 24:
        costo = 10
    return costo

lista_clienti: list[tuple] = [(1, 1.5), (2, 4.0), (3, 24.0)]
print(lista_clienti)

print(f"{'Car':<10}{'Hours':<15}{'Charge':<10}")
ore_totali:float = 0
somma_toale:float = 0

for car, ore in lista_clienti:
    costo = costo_parcheggio(ore)
    ore_totali += 0
    somma_toale += costo
    print(f"{car:<10}{ore:<15}{f'{costo:.2f}$':<10}")
 
print(f"{'Total':<10}{ore_totali:<15}{f'{somma_toale:.2f}$':<10}")