'''
Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.
For example:
Test                                     	Result
print(somma_elementi([1,1,1],[1,1,1]))     [2, 2, 2]
'''

def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    z:list = []
    for i in range(len(x)):
        z.append(x[i]+y[i])
    return z

print(somma_elementi([1,1,1],[1,1,1]))


for i in range(1,4):
    print(i)