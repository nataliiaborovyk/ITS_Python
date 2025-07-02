'''
Scrivi una funzione che, data una lista, 
ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
print(frequency_dict(['mela', 'banana', 'mela']))     Result    {'mela': 2, 'banana': 1}
'''

def frequency_dict(elements: list) -> dict:

    lista:list = []
    diz:dict = {}

    for i in elements:
        if i in lista:
            diz[i] += 1
        else:
            lista.append(i)
            diz[i] = 1

    return diz
    
print(frequency_dict(["mela", "banana", "mela"]))            #{'mela': 2, 'banana': 1}
print(frequency_dict([1, 2, 2, 3, 3, 3]))                    #{1: 1, 2: 2, 3: 3}
print(frequency_dict([]))                                    #{}
print(frequency_dict(['a', 'b', 'c', 'a', 'b', 'c', 'a']))   #{'a': 3, 'b': 2, 'c': 2}
print(frequency_dict([True, False, True]))                   #{True: 2, False: 1}
	


