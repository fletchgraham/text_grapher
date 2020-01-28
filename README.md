# Text Grapher: 2D & 3D Graphics Rendered as Text

![](img/cube_example.gif)

## Intro

**What is Text Grapher?** Text Grapher is a graphics library for rendering graphics using text. Rather than drawing lines using pixels in an image, it draws lines using characters in a string. 2D and 3D animations can quickly be composed and rendered as a series of text files or a gif.

**For what purpose?** The purpose of this python project is educational. Before this project I had been using 3D software every day without understanding what was happening under the hood. Putting this project together forced me to derive key concepts that make 3D software tick. Writing the Text Grapher API helped me understand how Blender's API works and where its structure comes from. 

**I'm currently working on [this notebook](text_grapher.ipynb), which documents my process of developing Text Grapher.**

## Quickstart

The following code is from the cube example that comes with Text Grapher. 

```python
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
#scene.render(open_player=True)
scene.render_gif(invert=True)
```

## Run the Other Examples:

There is also an animated lissajous curve, a fireworks animation. 

1. install Python 3.X
1. clone this repository.
1. `cd` into it.
1. run:

`python -m tg_examples.lissajous` or
`python -m tg_examples.fireworks` or
`python -m tg_examples.cube`

A window will appear and play the animation.

## Contributing

The best way to contribute at the moment is to write some cool examples!

![](img/example_01.jpg)
