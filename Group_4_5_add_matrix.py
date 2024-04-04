def add_matrices(matrix1, matrix2):
    matrix_new = matrix1
    if len(matrix1) != len(matrix1[0]) or len(matrix2) != len(matrix2[0]) or len(matrix1)!= len(matrix2):
        result = 'matrices must be quadratic and of equal demensions'
    else:
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                matrix_new[i][j] = matrix1[i][j]+matrix2[i][j]
        result = matrix_new
    return result

print(add_matrices([[1,1],[1,1]], [[1,1],[1,1]]))