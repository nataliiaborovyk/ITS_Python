'''
Scrivi una funzione min_per_riga(mat) che riceve una matrice mat: list[list[int]]
e restituisce una lista con il minimo di ogni riga.
'''
def min_per_riga(mat):
    lista_min: list = []
    for i in mat:
        mn: int = min(i)
        lista_min.append(mn)
    return lista_min
