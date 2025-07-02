'''
La funzione dovrebbe determinare se un elemento è presente in una lista.
Un errore nell'implementazione porta a risultati inaspettati.
'''

def find_element(lst: list[int], element: int) -> bool:
    if element in lst:
        return True
    else:
        return False
    

print(find_element([1, 2, 3, 4, 5], 5))    #True
print(find_element([1, 2, 3, 4, 5], 6))    #False
print(find_element([10, 20, 30], 20))      #True
