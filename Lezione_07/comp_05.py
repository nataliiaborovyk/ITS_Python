'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti 
che hanno un prezzo superiore a 20, ma scontati del 10%.

For example:
Test 	Result

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))   {'Zaino': 45.0, 'Quaderno': 19.8}

print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))     {}
'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    diz_nuovo:dict = {}
    for k, v in prodotti.items():
        if v > 20:
            diz_nuovo[k] = v * 0.9

    return diz_nuovo

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))  