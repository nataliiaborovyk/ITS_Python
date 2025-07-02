'''
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista.
print(remove_elements({5, 6, 7}, [7, 8, 9]))   Result  {5, 6}
'''

#VERSIONE 1

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

    for i in elements_to_remove:
        if i in original_set:
            original_set.remove(i)
    return original_set

print(remove_elements({1, 2, 3, 4}, [2, 3]))        #{1, 4}
print(remove_elements({5, 6, 7}, [7, 8, 9]))        #{5, 6}
print(remove_elements({1, 2}, [3]))                 #{1, 2}
print(remove_elements(set(), [1, 2, 3]))            #set()
print(remove_elements({10, 20, 30}, []))            #{10, 20, 30}



# VERSIONE 2

def remove_elements_2(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

    return {element for element in original_set if element not in elements_to_remove}

print("")
print(remove_elements_2({1, 2, 3, 4}, [2, 3]))        #{1, 4}
print(remove_elements_2({5, 6, 7}, [7, 8, 9]))        #{5, 6}
print(remove_elements_2({1, 2}, [3]))                 #{1, 2}
print(remove_elements_2(set(), [1, 2, 3]))            #set()
print(remove_elements_2({10, 20, 30}, []))            #{10, 20, 30}

        