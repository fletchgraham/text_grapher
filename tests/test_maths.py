from text_grapher.maths import (
    matrix_product,
    vector_to_matrix,
    matrix_to_vector,
    Vector
    )

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
