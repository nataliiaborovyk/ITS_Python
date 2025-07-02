'''
Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori.

For example:print(merge_dictionaries({'x': 5}, {'x': -5}))
Test 	Result {'x': 0}
'''

#VERSIONE 1

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
  
    dict3 = {}

    if dict1 == {} and dict2 != {}:
        return dict2
    elif dict1 != {} and dict2 == {}:
        return dict1
        
    for k1, v1 in dict1.items():
        if k1 in dict2:
            dict3[k1] = v1 + dict2[k1]
        else:
            dict3[k1] = v1
        
    for k2, v2 in dict2.items():
        if k2 not in dict3:
            dict3[k2] = v2

    return dict3
    

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dictionaries({}, {'a': 10, 'b': 20}))
print(merge_dictionaries({'x': 5}, {'x': -5}))
print(merge_dictionaries({}, {}))
print(merge_dictionaries({'a': 3}, {'b': 4}))


# VERSIONE 2

def merge_dictionaries_2(dict1: dict, dict2: dict) -> dict:
   
    dict3:dict = dict1.copy()

    for k, v in dict2.items():
        if k in dict3:
            dict3[k] += v
        else:
            dict3[k] = v

    return dict3

print("")
print(merge_dictionaries_2({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dictionaries_2({}, {'a': 10, 'b': 20}))
print(merge_dictionaries_2({'x': 5}, {'x': -5}))
print(merge_dictionaries_2({}, {}))
print(merge_dictionaries_2({'a': 3}, {'b': 4}))
