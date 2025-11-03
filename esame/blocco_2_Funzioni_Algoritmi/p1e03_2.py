'''
Scrivi una funzione max_per_colonna(mat) che restituisce una lista con
il massimo di ogni colonna della matrice.
'''
def max_per_colonna(mat):

    num_r:int = len(mat)
    num_c:int = len(mat[0])

    lista_max = []

    for index_c in range(num_c):
        lista = []
        for index_r in range(num_r):
            lista.append(mat[index_r][index_c])
        mx = max(lista)
        lista_max.append(mx)
    return lista_max