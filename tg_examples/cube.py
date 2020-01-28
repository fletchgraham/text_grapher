import text_grapher as tg

scene = tg.Scene()
scene.name = 'cube_example'

cube = tg.Cube()
scene.add(cube)

@scene.animation
def cube_rotation(t):
    cube.rotate(.01, .01, .01)

scene.render(open_player=True)
