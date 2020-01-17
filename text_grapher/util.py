

def matrix_product(A, B):

    C = [[0 for i in A] for j in B]

    for i in range(len(A)):

        for j in range(len(B[0])):

            for k in range(len(B)):

                C[i][j] += A[i][k] * B[k][j]

    return C

def vector_to_matrix(vector):
    M = [[i] for i in vector]
    M.append([1])
    return M

def matrix_to_vector(matrix):
    return tuple([i[0] for i in matrix[:-1]])
