'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.
'''
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    diz_scont:dict [str:float] = {}
    for prod, prez in prodotti.items():
        if prez > 20:
            sconto:float = round((prez - prez * 0.1),2)
            diz_scont[prod] = sconto
    return diz_scont

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
