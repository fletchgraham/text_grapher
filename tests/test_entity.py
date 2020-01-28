from text_grapher import Vector
from text_grapher.entities import Entity


def test_entity_rotation():
    ob = Entity()

    assert ob.rotation.x == 0
    ob.rotate(30)
    assert ob.rotation.x == 30

    ob.rotate(z=10)
    assert ob.rotation.z == 10

def test_entity_scale():
    ob = Entity()
    assert ob.scale == Vector(1,1,1)

    ob.resize(x=3)
    ob.resize(x=.5)
    assert ob.scale.x == 1.5

def test_enity_translate():
    ob = Entity()
    assert ob.location.z == 0

    ob.translate(z=15.4)
    assert ob.location == Vector(0,0,15.4)
