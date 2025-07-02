'''
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))   Result  2
print(count_isolated([1, 2, 3, 4, 5]))                 5
'''


#VERSIONE 1

def count_isolated(lista:list[int]) -> int:
  
    cont:int = 0
    x:int = len(lista)
    for i in range(x):
        if i == 0: 
            if lista[0] != lista[1]:
                cont += 1
        elif i == x-1:
            if lista[i-1] != lista[i]:
                cont += 1
        else: 
            if lista[i] != lista[i+1] and lista[i] != lista[i-1]:
                cont += 1
    return cont 
       
    

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))    #2
print(count_isolated([1, 1, 2, 2, 3, 4, 4]))    #1
print(count_isolated([1, 2, 3, 4, 5]))          #5
print(count_isolated([1, 1, 1, 1, 1]))          #0
print(count_isolated([]))                       #0


# VERSIONE 2

def count_isolated_2(lista:list[int]) -> int:
    cont:int = 0
    for i in range(len(lista)):
        if (i == 0 or lista[i] != lista[i-1]) and (i == len(lista)-1 or lista[i] != lista[i+1]):
            cont += 1
    return cont
  
print("")
print(count_isolated_2([1, 2, 2, 3, 3, 3, 4]))    #2
print(count_isolated_2([1, 1, 2, 2, 3, 4, 4]))    #1
print(count_isolated_2([1, 2, 3, 4, 5]))          #5
print(count_isolated_2([1, 1, 1, 1, 1]))          #0
print(count_isolated_2([]))                       #0