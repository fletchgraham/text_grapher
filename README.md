# Text Grapher: 2D & 3D Graphics Rendered as Text

![](img/cube_example.gif)

## Intro

**What is Text Grapher?** Text Grapher is a graphics library for rendering graphics using text. Rather than drawing lines using pixels in an image, it draws lines using characters in a string. 2D and 3D animations can quickly be composed and rendered as a series of text files or a gif.

**For what purpose?** Text Grapher is mostly an educational novelty. Before this project I had been using 3D software every day without understanding what was happening under the hood. Putting this library together forced me to derive key concepts that make 3D software tick. Writing the Text Grapher API helped me understand how Blender's API works and where its structure comes from. 

**I'm currently working on [this notebook](text_grapher.ipynb), which documents my process of developing Text Grapher.**

## Super Simple Example

The following code is from the cube example that comes with Text Grapher. 

```python
import text_grapher as tg

scene = tg.Scene()
scene.name = 'cube_example'

scene.graph.center_view()

cube = tg.Cube(size=2)
scene.add(cube)

@scene.animation
def cube_rotation(t):
    cube.rotate(.05, .05, .05)

scene.render(open_player=True)
```

Pretty simple right? We just create a scene, add a cube to it, define an animation and render it out. easy! 

The only lines here that aren't self explanatory are `scene.graph.center_view()` and the animation decorator. The former just centers the origin of the world in the middle of our graph. The latter is how we tell the scene what to animate: any function decorated with `@scene.animation` gets added to a list of functions that run at the begining of each frame. In this example we just rotated the cube a little bit each frame.

## Run the Other Examples:

There is also an animated lissajous curve, and a fireworks animation. 

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
