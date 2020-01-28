import pytest
from text_grapher.maths import *

def test_vector_init():
    vector = Vector()
    assert vector.x == 0
    assert vector.y == 0
    assert vector.z == 0

def test_add_vectors():
    v1 = Vector(1, 3, 4)
    v2 = Vector(2, 4, -10)
    assert Vector.add(v1, v2) == Vector(3, 7, -6)

def test_matrix_product():
    A = [[0, 1],
         [1, 0]]

    B = [[0, 0],
         [1, 0]]

    C = [[1, 0],
         [0, 0]]

    D = [[0, 0],
         [0, 1]]

    assert not matrix_product(A, B) == matrix_product(B, A)
    assert matrix_product(A, B) == C
    assert matrix_product(B, A) == D

def test_matrix_vector_conversions():
    v = Vector(2, 3, 4)
    m = vector_to_matrix(v)
    assert m == [[2], [3], [4], [1]]
    v2 = matrix_to_vector(m)
    assert v2 == v

# Transformations:

def test_rotate_vector():
    v1 = Vector(1, 0, 0)
    R = rotation_matrix(z = 3.141/2)
    v2 = Vector.transform(v1, R)

    print(v2)
    assert v2.y == pytest.approx(-1)

def test_translate_vector():
    v1 = Vector(0, 1, 0)
    T = translation_matrix(5, 3, 5)
    v2 = Vector.transform(v1, T)
    assert v2 == (5, 4, 5)

def test_scale_vector():
    v1 = Vector(2, 2, 0)
    S = scale_matrix(3, 4, 0)
    v2 = Vector.transform(v1, S)
    assert v2 == (6, 8, 0)

def test_multiple_transforms():
    v1 = Vector(1, 0, 0)
    S = scale_matrix(3, 3, 3)
    R = rotation_matrix(y = 3.14159)
    T = translation_matrix(y=-1)
    M = matrix_product(R, S)
    M = matrix_product(T, M)
    v2 = Vector.transform(v1, M)
    assert v2.y == pytest.approx(-1)
    assert v2.x == pytest.approx(-3)
    assert v2.z == pytest.approx(0, abs=1e-3) # set wider tolerance
