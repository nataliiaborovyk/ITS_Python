'''
Scintille Divergenti

Due distillati rivelano impurità reciproche: registra i componenti esclusivi. 
Con `symdiff_sorted(a, b)` ritorna gli interi che stanno in una sola lista, 
in ordine crescente. 
Mantieni la firma e chiarifica i test.
'''

def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = list(set(a) ^ set(b))
    return sorted(set(c))

# alternativa

def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    return sorted(set(a) ^ set(b))


def symdiff_sorted2(a: list[int], b: list[int]) -> list[int]:
    lista:list =[]
    s1:set = set(a)
    s2:set = set(b)
    s: set = s1.copy()
    s.update(s2)  # oppure direttamente s = s1.union(s2)
    for i in s:
        if ((i in s1) and (i not in s2)) or ((i in s2) and (i not in s1)):
            lista.append(i)
    print(lista)

    lista_ord: list = []
    for i in range(len(lista)):
        m:int = min(lista)
        lista_ord.append(m)
        lista.remove(m)
        
    lista_ord: list = []

    copia: list = lista.copy()
    while copia:
        n_m = copia[0]
        ind_n_m = 0
        for i in range(1, len(copia)):
            if copia[i] < n_m:
                n_m = copia[i]
                ind_n_m = i
        lista_ord.append(n_m)
        copia.pop(ind_n_m)

    


    return lista_ord
    
a=[20,1,6,3,6,4,8,7,8,9]
b=[3,2,5,3,7,8,5,4,3,2,1]
print(symdiff_sorted2(a,b))