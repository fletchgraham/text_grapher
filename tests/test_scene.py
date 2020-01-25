import text_grapher as tg

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

    assert scene.graph.width == 40
    assert scene.graph.height == 40

    scene.graph.width = 80
    assert scene.graph.width == 80

    scene.graph.height = 80
    assert scene.graph.height == 80

def test_render():
    scene = tg.Scene()

    @scene.animate
    def my_animation(t):
        scene.graph.background = f'{t}'
        scene.graph.clear()

    scene.frame(7)
    print(scene.graph)
    assert '6' in scene.graph._array[5]
