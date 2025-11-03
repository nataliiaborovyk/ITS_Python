'''
B1.I.1 — Balanced Load Index (liste)

Task. Dato arr: list[int] (len ≥ 1), si definisce balanced load index l’indice k tale che
 la somma dei valori in posizioni dispari a sinistra di k sia uguale alla somma dei valori
   in posizioni pari a destra di k.  Restituire l’indice k se esiste, altrimenti None.
Input. arr può contenere negativi.
Output. int | None.
Vincoli. Non usare librerie esterne; un solo passaggio “pesante” sulla lista è preferibile.
Esempio. arr=[5,1,2,3,2] → k=2 (sinistra-dispari: pos 1→1; destra-pari: 
pos 4→2; ma verifica con definizione completa).
'''

def balanced_load_index(array: list[int]) -> int | None:
    for index in range(len(array)):
        somma_disp: int = sum(array[x] for x in  range(0,index) if x % 2 != 0 )
        somma_pari:int = sum(array[x] for x in  range(index+1, len(array)) if x % 2 == 0 )
        if somma_disp == somma_pari:
            return index
    return None
    

def balanced_load_index1(array: list[int]) -> int | None:
    for index in range(len(array)):
        somma_disp: int = sum(array[1:index:2] )
        if index % 2 == 0:
            somma_pari:int = sum(array[index+2::2])
        else:
            somma_pari:int = sum(array[index+1::2])
        if somma_disp == somma_pari:
            return index
    return None
    
def balanced_load_index3(array:list[int]) -> int |None:
    n=len(array)
    somma_pari:int = sum(array[x] for x in range(0,n,2))
    somma_dispari:int = 0
    for index in range(n):
        if index % 2 == 0:
            somma_pari -= array[index]
        if somma_dispari == somma_pari:
            return index
        if index % 2 == 1:
            somma_dispari += array[index]
    return None
        


balanced_load_index3([5,1,2,3,2])

