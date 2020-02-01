===============
Getting Started
===============

***********************
Printing a Simple Graph
***********************

The graph object is the canvas onto which graphics are drawn.
It exists conceptually as a 2D array, the cells of which can be filled with
characters in order to represent shapes or functions.

Let's create a graph object.

>>> import text_grapher as tg
>>> graph = tg.Graph(11, 11)
>>> print(graph)
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .

Let's see where the point (0, 0) is on this graph.

>>> graph.plot(0, 0, '@')
>>> print(graph)
@ . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .

By default, (0, 0) is in the upper left corner and Y values increase toward the
bottom. Unless you do a lot of GUI programming, you're probably more
comfortable with the origin of the graph at the center with Y values increasing
toward the top. The graph object has a method to accomplish this.

>>> graph.clear()
>>> graph.center_view()
>>> graph.plot(0, 0, '@')
>>> print(graph)
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . @ . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
