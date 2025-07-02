'''
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali
'''

def prod(diz:dict[str,float]) -> dict:
    diz_nuovo:dict = {}
    for k,v in diz.items():
        if v < 50:
            diz_nuovo[k] = round(v + v*0.1, 2)
    return diz_nuovo

diz:dict = {"latte": 5, "pane": 55}
print(prod(diz))