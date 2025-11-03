'''
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
'''
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict_unito:dict = dict1.copy()
    for k, v in dict2.items():
        if k not in dict_unito:
            dict_unito[k] = v
        else:
            dict_unito[k] += v
    return dict_unito