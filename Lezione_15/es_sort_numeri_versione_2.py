'''
Data una lista di numeri disordinata, dobbiamo metterla in ordine dal piu piccolo al piu grande usando solo cicli
''' 

def lista_ordinata_2(lista:list) -> list:
    lung:int = len(lista)
    for i in range(lung):
        m = i
        for k in range(i+1, lung):    #quando m=lung-1 ciclo no parte perke k=lung
            print(f"m={m}, k={k}")
            print(f"Lista m[{m}]= {lista[m]}, Lista k[{k}]={lista[k]}")
            if lista[m] > lista[k]: #se succesivo elemento piu grande aggiorno indice di partenza
                print(f"!!!in questo caso {lista[m]} > {lista[k]} -> m \"{m}\" = k \"{k}\"\n")
                m = k
                #trovo elemento piu piccolo in iterazione e lo metto al primo posto di questa itarazione
            else:
                print("non sucede niente\n")
            
        lista[i], lista[m] = lista[m], lista[i]
        print(lista)
        print(f"____________finito i = {i}\n")

    return lista
print(lista_ordinata_2([5,12,4]))
