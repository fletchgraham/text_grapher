"""Math concepts like vectors and matrices"""

from math import sin, cos
from collections import namedtuple

def identity_matrix():
    """Return an identity matrix

    This is a function instead of a global variable because you want to know
    it hasn't been altered."""

    return [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

class Vector(namedtuple('Vector', ['x', 'y', 'z'], defaults=[0,0,0])):

    @classmethod
    def add(cls, v1, v2):
        return Vector(
            v1.x + v2.x,
            v1.y + v2.y,
            v1.z + v2.z
            )

    @classmethod
    def transform(cls, vector, matrix):
        """Return a new vector with the transformation matrix applied"""
        P = vector_to_matrix(vector)
        M = matrix
        MP = matrix_product(M, P)
        new_vector = matrix_to_vector(MP)
        return new_vector

def matrix_product(A, B):
    """Return the matrix product: AB"""
    C = [[0 for i in A] for j in B]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

def vector_to_matrix(vector):
    """Return an iterable like a Vector as a matrix"""
    M = [[i] for i in vector]
    M.append([1])
    return M

def matrix_to_vector(matrix):
    """Return a Tuple from a matrix... this should return a Vector"""
    if len(matrix) == 4:
        x = matrix[0][0]
        y = matrix[1][0]
        z = matrix[2][0]
        return Vector(x, y, z)
    else:
        return tuple([i[0] for i in matrix[:-1]])

def rotation_matrix(x=0, y=0, z=0):
    """Return a rotation matrix for the given rotation.

    The parameters result in clockwise rotation in radians around each axis.
    """
    m = identity_matrix()

    rot_x = [[1, 0, 0, 0],
             [0, cos(x), sin(x), 0],
             [0, -sin(x), cos(x), 0],
             [0, 0, 0, 1]]

    rot_y = [[cos(y), 0, -sin(y), 0],
             [0, 1, 0, 0],
             [sin(y), 0, cos(y), 0],
             [0, 0, 0, 1]]

    rot_z = [[+cos(z), +sin(z), 0, 0],
             [-sin(z), +cos(z), 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]

    p = matrix_product(rot_x, m)
    p = matrix_product(rot_y, p)
    p = matrix_product(rot_z, p)

    return p

def translation_matrix(x=0, y=0, z=0):
    """Return a translation matrix for the given translation values."""
    m = identity_matrix()

    translate_m = [[1, 0, 0, x],
                 [0, 1, 0, y],
                 [0, 0, 1, z],
                 [0, 0, 0, 1]]

    p = matrix_product(translate_m, m)
    return p

def scale_matrix(x=0, y=0, z=0):
    """Return a scale matrix for the given scale factor."""

    m = identity_matrix()
    scale_m = [[x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]]

    p = matrix_product(scale_m, m)
    return p

def transform_verts(verts_list, matrix):
    """Return a new list of verts with the matrix applied"""
    return [Vector.transform(vert) for vert in verts_list]
