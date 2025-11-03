'''
### **B2.I.3 — Matrix Saddle Points (funzioni pure)**

**Task.** Data una matrice rettangolare `mat: list[list[int]]`, 
trova tutte le **celle che sono minime nella loro riga e massime nella loro colonna**.
**Output.** Lista di tuple `(r_idx, c_idx, value)` ordinate per riga e colonna.
**Esempio.**
mat = [
 [2, 1, 9],
 [8, 5, 6],
 [3, 4, 2]
]
→ output: `[(1,1,5)]` 
(perché 5 è il minimo sulla sua riga [8,5,6] e massimo sulla colonna [1,5,4]).
'''

def matrix(mat:list[list[int]]) -> list[tuple]:

    if not mat or not mat[0]:
        return []
    
    set_min: set = set()
    set_max: set = set()

    for index_r in range(len(mat)):
        mn = min(mat[index_r])
        for index_c in range(len(mat[index_r])):
            if mat[index_r][index_c] == mn:
                set_min.add((index_r, index_c, mn))
    

    for index_c in range(len(mat[0])):
        lista_col:list = []
        for index_r in range(len(mat)):
            lista_col.append(mat[index_r][index_c])
        mx = max(lista_col)
        for index_r in range(len(mat)):
            if mat[index_r][index_c] == mx:
                set_max.add((index_r, index_c, mx))
    
    result_set = set_min & set_max
  
    result = sorted(result_set, key=lambda t: (t[0], t[1]))
    return result



def saddle_points2(mat: list[list[int]]) -> list[tuple[int, int, int]]:
    if not mat or not mat[0]:
        return []
    n_rows, n_cols = len(mat), len(mat[0])

    row_mins = [min(row) for row in mat]
    col_maxs = [max(mat[r][c] for r in range(n_rows)) for c in range(n_cols)]

    out = []
    for r in range(n_rows):
        for c in range(n_cols):
            v = mat[r][c]
            if v == row_mins[r] and v == col_maxs[c]:
                out.append((r, c, v))
    out.sort(key=lambda t: (t[0], t[1]))
    return out

