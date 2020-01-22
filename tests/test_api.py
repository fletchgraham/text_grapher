import text_grapher as tg

def test_scene_init():
    scene = tg.Scene()
    assert scene.frame_start == 1
    assert scene.camera.location == (0,0,10)

def test_mesh_init():
    mesh = tg.Mesh()

    assert mesh.location == (0, 0, 0)
    assert mesh.rotation == (0, 0, 0)
    assert mesh.scale_factor == (1, 1, 1)

    assert mesh.character == 'M'

    assert mesh.vertices == []
    assert mesh.edges == []
