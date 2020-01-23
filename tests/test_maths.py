from text_grapher.maths import matrix_product

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
