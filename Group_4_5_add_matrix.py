#READ ME

#Description:
#The function add_matrices takes two matrices of equal dimensions and returns
#one matrix in which each element is the sum of the corresponsing elements in the input matrices

#Parameters:
#matrix1 and matrix2 are two matrices given as lists of lists; they must be of equal dimensions

#Limitations
# -the function does not check whether the lists are proper matrices (sublists have equal lenght, etc.)

#Structures
# - an if-statement is used to check whether the matrices are of equal dimensions
# - two for loops nested into each other are used to access each element of both matrices, add them together
#   and write them into a new matrix

#Output
# The function returns one matrix in which each element is the sum of the corresponding elements in the input matrices


def add_matrices(matrix1, matrix2):
    matrix_new = matrix1
    if len(matrix1[0]) != len(matrix1[0]) or len(matrix1)!= len(matrix2):
        result = 'matrices must of equal dimensions'
    else:
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                matrix_new[i][j] = matrix1[i][j]+matrix2[i][j]
        result = matrix_new
    return result

print(add_matrices([[1,1],[1,1],[1,1]], [[1,1],[1,1],[1,1]]))