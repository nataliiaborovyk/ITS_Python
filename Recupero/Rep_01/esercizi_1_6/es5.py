'''
Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
'''


from typing import Union


def funzione2(lista:Union[int, float], treshold:int) -> int:
    prod:int = 1
    for i in lista:
        if type(i) == int:
            if i < treshold:
                prod *= i
        else:
            continue
    return prod

lista:list = [1,2,3,4,5]
print(funzione2(lista,3))
print(funzione2(lista,5))