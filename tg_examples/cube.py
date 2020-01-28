import text_grapher as tg

# the scene object keeps track of the camera, the graph,
# and the entities in the world
scene = tg.Scene()
scene.name = 'cube_example'

# centers the screen on the origin of the world
scene.graph.center_view()

# add a cube to the scene
cube = tg.Cube(size=2)
scene.add(cube)

# define an animation,
# this will run before each frame is drawn
@scene.animation
def cube_rotation(t):
    cube.rotate(.05, .05, .05)

# writes the frames as text files
# and open a player to view them as an animation
scene.render(open_player=True)
