'''
### B1.I.3 — Merge Inventories (dizionari)

**Task.** Dati due dizionari inventario `invA: dict[str,int]`, `invB: dict[str,int]`, 
creare `merge_inventories(invA, invB) -> dict[str,int]` che:
    * somma le quantità per le chiavi comuni;
    * rimuove dal risultato gli item con quantità finale `≤ 0`;
    * restituisce le chiavi **ordinate alfabeticamente** (come lista) 
    e il dizionario risultante (tuple `(keys_sorted, merged_dict)`).

  **Esempio.** `{"apple":2,"banana":-1}`, `{"banana":3,"cherry":1}` → 
  keys `['apple','banana','cherry']`, dict `{'apple':2,'banana':2,'cherry':1}`.
'''

def merge_inventories(invA:dict, invB:dict) -> dict[str,int]:
    fin:dict = {}
    for k1, v1 in invA.items():
        if k1 in invB:
            if v1 + invB[k1] > 0:
                fin[k1] = v1 + invB[k1]
        else:
            if v1 > 0:
                fin[k1] = v1
    for k2, v2 in invB.items():
        if k2 not in fin:
            if v2 > 0:
                fin[k2] = v2
    keys:list = sorted(fin.keys())
    return keys, fin

print(merge_inventories({"apple":2,"banana":-1}, {"banana":3,"cherry":1}))
    
                
            