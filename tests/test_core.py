import text_grapher as tg
from text_grapher.core import Entity

def test_scene_naming():
    scene = tg.Scene()
    # default name
    assert scene.name == 'tg_scene'

    # test rename
    new_name = 'my_3d_scene'
    scene.name = new_name
    assert scene.name == new_name

    # test init with name
    another_scene = tg.Scene('fred')
    assert another_scene.name == 'fred'

def test_render_dims():
    scene = tg.Scene()

    assert scene.render_width == 40
    assert scene.render_height == 40

    scene.render_width = 80
    assert scene.render_width == 80

    scene.render_height = 80
    assert scene.render_height == 80

def test_entity_rotation():
    ob = Entity()

    assert ob.rotation.x == 0
    ob.rotate(30)
    assert ob.rotation.x == 30

    ob.rotate(z=10)
    assert ob.rotation.z == 10

def test_entity_scale():
    ob = Entity()
    assert ob.scale == tg.Vector(1,1,1)

    ob.resize(x=3)
    ob.resize(x=.5)
    assert ob.scale.x == 1.5

def test_enity_translate():
    ob = Entity()
    assert ob.location.z == 0

    ob.translate(z=15.4)
    assert ob.location == tg.Vector(0,0,15.4)
