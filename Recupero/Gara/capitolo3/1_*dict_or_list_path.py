'''
Nelle linee di distillazione annidate segui la mappa passo dopo passo, 
altrimenti ricorri alla dose di sicurezza. Implementa `deep_get(d, path, default)`, 
avanzando tra dizionari e liste `d` seguendo `path`; 
restituisci il passo ma, se manca, ritorna `default`. 
Mantieni la firma e supera i test.
'''


def deep_get(d: dict | list, path: list, default=None):
    if path == []:
        return d
    passo = d  # cosi entro dentro a ogni ciclo
    for i in path:
        if type(passo)is dict:
            if i in passo:
                passo = passo[i]
            else: 
                return default
        elif type(passo) is list:
            if type(i) is int:
                if -len(passo) <= i < len(passo):
                    passo = passo[i]
                else:
                    return default
            else:
                return default
        else:
            return default
    return passo


# alternative

def deep_get(d: dict | list, path: list, default=None):
    if not path:
        return d

    cur = d
    for step in path:
        try:
            # Per i dict: cur[step] -> KeyError se manca
            # Per le list: cur[step] -> IndexError/TypeError se step non è un indice valido
            cur = cur[step]
        except (KeyError, IndexError, TypeError):
            return default
    return cur
