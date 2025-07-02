'''
Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.
'''

def ricercaBinaria(lista: list[int], x:int) -> bool:
    result: bool = False
    indice_min: int = 0
    indice_max: int = len(lista) - 1
    while result != True and indice_min <= indice_max:
        indice_medio = (indice_min + indice_max) // 2 
        if lista[indice_medio] == x:
            result = True
        elif lista[indice_medio] > x:
            indice_max = indice_medio - 1
        else:
            indice_min = indice_medio + 1
    return result


                
if __name__ == "__main__":
    lista1: list = [1,2,3,4,5,6,7,8,9,10]
    lista2: list = [1,2,3,4,5,6,7,8,9,10,11]
    lista3: list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    print(ricercaBinaria(lista1, 6))
    print(ricercaBinaria(lista1, 11))
    print(ricercaBinaria(lista2, 10))
    print(ricercaBinaria(lista3, 11))

        
        