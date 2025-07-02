
def sum_secondary_diagonal(matrix:list[list[int]]) -> int:
    somma:int = 0
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if k == (len(matrix[i]) - 1 - i):
                somma += matrix[i][k]
    return somma


if __name__ == "__main__":
    mat1 = [
        [1, 2, 1, 3],
        [4, 1, 5, 6],
        [1, 7, 8, 9],
        [1, 7, 8, 9],
    ]
    print(sum_secondary_diagonal(mat1))

    '''
    i=0, k=3  3-0=3
    i=1, k=2  3-1=2
    i=3, k=1  3-3=1
    i=3, k=0  3-0=0
    '''

    mat2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(sum_secondary_diagonal(mat2))