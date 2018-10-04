from fletch_tools.good_input import get_input
from tg_utils.grapher import *

def graph(args):

    char = ' ' + get_input('Enter a character to represent empty space.')[0]
    draw_char = ' ' + get_input('Enter a character with which to draw the object.')[0]
    dst = get_input('Enter a name for the folder of text files.')

    # build a blank grid
    my_blank = BlankGraph(size=44, char=char)
    my_graph = my_blank.build()

    # create a camera
    my_camera = Camera(location=[0, 0, -16], rotation=[0, 0, 0])

    # create cube
    my_cube = Mesh(location=[0,0,0], rotation=[pi/8, pi/4, pi/16], scale=[2, 2, 2])

    my_camera.draw(my_graph, my_cube, draw_char)

    joined = "".join(my_graph)
    print(joined)

    rotate_animation(pi/128, 2*pi, char, draw_char, dst)

def wh_help(args=''):
    if args:
        print("\n{}'{}' didn't trigger any commands!"
            .format('  ', ' '.join(args)))
    else:
        print(
            '\n  Text Grapher'
            )
    print(
        """
  Commands:

  wh help              - Show help and exit.
  wh graph             - Fire up the graphing process.
        """
    )
