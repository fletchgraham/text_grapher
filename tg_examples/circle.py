"""A circle that grows and shrinks based on the sine of the frame number"""

from math import sin
import text_grapher as tg

# create a scene and name it
scene = tg.Scene()
scene.name = 'circle_example'

# A small graph for this example
scene.graph.width = 11
scene.graph.height = 11

# roughly the period of a sine wave multiplied by ten
scene.graph.frame_stop = 32

# put (0, 0) at the center of the graph
scene.graph.center_view()

# use the decorator to define our animation
@scene.animation
def circle_animation(frame):
    radius = (sin(frame / 10) + 1) * 3 # oscillating radius
    scene.graph.circle(0, 0, radius, '@')

# render the scene and play it in the GUI
scene.render(open_player=True)
