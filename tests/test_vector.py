from text_grapher.util import Vector, vector_add


def test_vector_init():
    vector = Vector()
    assert vector.x == 0
    assert vector.y == 0
    assert vector.z == 0

def test_add_vectors():
    v1 = Vector(1, 3, 4)
    v2 = Vector(2, 4, -10)
    assert vector_add(v1, v2) == Vector(3, 7, -6)
