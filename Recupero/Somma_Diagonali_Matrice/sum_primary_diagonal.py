
def sum_primary_diagonal(matrix:list[list[int]]) -> int:
    somma:int = 0
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if i == k:
                somma += matrix[i][k]
    return somma



if __name__ == "__main__":
    mat1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    print(sum_primary_diagonal(mat1))