import os
import shutil
import text_grapher as tg
from math import sin, cos

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

def test_get_frame():
    scene = tg.Scene()

    @scene.animate
    def my_animation(t):
        scene.graph.background = f'{t}'
        scene.graph.clear()

    scene.frame(7)
    print(scene.graph)
    assert '6' in scene.graph._array[5]

def test_render():
    scene = tg.Scene()

    @scene.animate
    def lissajous(t):
        x = cos(3 * t) * 18 + 20
        y = sin(4 * t) * 18 + 20
        scene.graph.plot(x, y, u"\u2584")

    scene.render()
    assert os.path.exists(scene.name)
    with open(os.path.join(scene.name, '00004.txt'), 'r') as infile:
        assert u"\u2584" in infile.read()

    shutil.rmtree(scene.name)
