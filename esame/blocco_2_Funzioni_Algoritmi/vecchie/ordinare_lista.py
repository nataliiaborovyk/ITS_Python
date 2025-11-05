'''
Data una lista di numeri disordinata, dobbiamo metterla in ordine dal piu piccolo al piu grande usando solo cicli
'''

def ordine(lista:list[int]):
    for i in range(len(lista)):
        for k in range(i+1, len(lista)):
            if lista[k] < lista[i]:
                lista[i], lista[k] = lista[k], lista[i]
    return lista

l1 = [5,2,4,3,7]
print(ordine(l1))

                    