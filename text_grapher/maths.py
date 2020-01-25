"""Math concepts like vectors and matrices"""

from collections import namedtuple

class Vector(namedtuple('Vector', ['x', 'y', 'z'], defaults=[0,0,0])):

    @classmethod
    def add(cls, v1, v2):
        return Vector(
            v1.x + v2.x,
            v1.y + v2.y,
            v1.z + v2.z
            )

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
