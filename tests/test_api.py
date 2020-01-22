import text_grapher as tg

def test_scene_init():
    scene = tg.Scene()
    assert scene.frame_start == 1
