'''
### B1.I.2 — Deduplicate & Preserve (liste, set)

**Task.** Funzione `dedup_preserve(nums: list[int]) -> list[int]`
 che rimuove i duplicati **preservando l’ultima occorrenza** (non la prima).
**Output.** Lista risultante nell’**ordine originale** delle occorrenze *sopravvissute*.
**Esempio.** `[3,1,3,2,1,3]` → `[2,1,3]`.
'''

def dedup_preserve(num:list[int]) -> list[int]:
    for index in range(len(num)):
        if num[index] in num[index+1:]:
            num[index] = None
    list2:list = []
    for el in num:
        if el != None:
            list2.append(el)
    return list2

def dedup_preserve1(num:list[int]) -> list[int]:
    doppi:set = set()
    nuovo:list = []
    n:int = len(num)
    for index in range(n-1, -1, -1):
        if num[index] not in doppi:
            nuovo.append(num[index])
            doppi.add(num[index])
    nuovo.reverse()
    return nuovo


print(dedup_preserve1([3,1,3,2,1,3]))