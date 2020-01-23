import text_grapher as tg

def test_scene_naming():
    #test getter for scene name
    scene = tg.Scene()
    assert scene.name == 'tg_scene'

    # test rename
    new_name = 'my_3d_scene'
    scene.name = new_name
    assert scene.name == new_name

    # test init with name
    another_scene = tg.Scene('fred')
    assert another_scene.name == 'fred'

def test_mesh_init():
    mesh = tg.Mesh()

    assert mesh.location == (0, 0, 0)
    assert mesh.rotation == (0, 0, 0)
    assert mesh.scale_factor == (1, 1, 1)

    assert mesh.character == 'M'

    assert mesh.vertices == []
    assert mesh.edges == []
