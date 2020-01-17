from text_grapher import util

def test_matrix_product():
    A = [[0, 1],
         [1, 0]]

    B = [[0, 0],
         [1, 0]]

    C = [[1, 0],
         [0, 0]]

    D = [[0, 0],
         [0, 1]]

    assert not util.matrix_product(A, B) == util.matrix_product(B, A)
    assert util.matrix_product(A, B) == C
    assert util.matrix_product(B, A) == D
