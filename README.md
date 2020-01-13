# Text Grapher: 3D Graphics Rendered as Text

![alt text](img/example_01.jpg)

## Intro

**What is Text Grapher?** Text Grapher is a graphics library for rendering geometries using text. Rather than drawing lines using pixels in an image, it draws lines using characters in a string.

**For what purpose?** The purpose of this python project is educational. When I started this project in 2017 I had been using 3d software for over a decade without understanding what was happening under the hood. It was also on my to-do list to learn python, so I set out to write a graphics library from scratch, with no third-party libraries like numpy. The research required to pull it off helped me answer the following questions:

- How are vectors represented in software?
- How are geometries defined?
- How can geometries be transformed using matrices?
- How can 3d space be represented on a 2d grid?
- What is object oriented programming?

**[View this notebook](text_grapher.ipynb) to see my process of developing Text Grapher.**


## Run the Example:

Text Grapher creates an animation of a cube spinning in space.
It uses provided characters to render each frame of the animation
as a .txt file. The animation can be watched by rapidly viewing
the text files in succession. OS X has the ability to preview files -
this works perfectly.

- install Python 3.X
- clone this repository.
- `cd` into it.
- run `pip install .`
- `cd` to where you want to save the generated text files.
- run `tg graph` and answer the prompts.
- open the generated folder to find your text files.
