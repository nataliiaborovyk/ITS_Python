'''
Sigillo Cercato

Negli annali delle formule cerchi un ingrediente: 
se manca sugli scaffali, prendi il sostituto previsto. 
Applica `get_or_default(d, k, default)` restituendo il valore o `default` senza alterare `d`. 
Mantieni la firma e supera i test.
'''

def get_or_default(d: dict, k, default=None):
    for i, j in d.items():
        if i == k:
            return j
    return default
        
def get_or_default(d: dict, k, default=None):
    if k in d:
        return d[k]
    else:
        return default