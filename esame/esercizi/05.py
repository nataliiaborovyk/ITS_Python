'''
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
'''

def frequency_dict(elements: list) -> dict:
    dict_frequenza: dict[str,int] = {}
    for el in elements:
        if el not in dict_frequenza:
            dict_frequenza[el] = 1
        else:
            dict_frequenza[el] += 1
    return dict_frequenza