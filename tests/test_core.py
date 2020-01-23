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

def test_entity_rotation():
    ob = Entity()
    assert ob.rotation.x == 0
    ob.rotate_x(30)
    assert ob.rotation.x == 30
