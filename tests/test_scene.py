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

    assert scene.render_width == 40
    assert scene.render_height == 40

    scene.render_width = 80
    assert scene.render_width == 80

    scene.render_height = 80
    assert scene.render_height == 80

def test_render():
    scene = tg.Scene()

    @scene.animate
    def my_animation(t):
        scene.background = f'{t}'

    graph = scene.graph_array(7)
    assert '7' in graph[5]
