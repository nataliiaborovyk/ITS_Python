'''
Scrivi una funzione celle_min_riga(mat) che restituisce una lista di tuple
(riga, colonna, valore) per tutte le celle che sono minime nella loro riga.
'''

def celle_min_riga(mat):

    lista_min = []

    for index_r in range(len(mat)):
        mn = min(mat[index_r])
        for index_c in range(len(mat[index_r])):
            if mat[index_r][index_c] == mn:
                lista_min.append((index_r, index_c, mn))
    
    return lista_min