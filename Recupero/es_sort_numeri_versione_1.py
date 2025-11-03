'''
Data una lista di numeri disordinata, dobbiamo metterla in ordine dal piu piccolo al piu grande usndo solo cicli
'''

def lista_ordinata(lista:list) -> list:
    for i in range(len(lista)):
        
        for k in range(len(lista)):
            print(f"adesso i = {i} k = {k}")
            print(f"Lista i[{i}] = {lista[i]}")
            print(f"Lista k[{k}] = {lista[k]}")
            
            if lista[i] >= lista[k]:    ##########
                print(f"non sucede niente")
            else:
                print(f"lista k[{k}]={lista[k]} si cambia con lista i[{i}]={lista[i]}")
                lista[i], lista[k] = lista[k], lista[i]
                print(f"Lista i[{i}] = {lista[i]}")
                print(f"Lista k[{k}] = {lista[k]}")
                
            print(lista, "\n")           
            print(f"____finito k = {k}\n")
        print(f"____________finito i = {i}\n")
    
    return lista

print(lista_ordinata([11,7,5]))
 