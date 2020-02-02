===============
Getting Started
===============

************
Installation
************

TO DO

****************
Printing a Graph
****************

Because this library is all about creating visuals with text, Printing your
first graph is easy to achieve and can be done from the Python REPL.

The graph object is the canvas onto which graphics are drawn.
It exists conceptually as a 2D array, the cells of which can be filled with
characters in order to represent shapes or functions.

The following example shows the three lines necessary to create and show
a blank graph.

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

******************
Graphing Equations
******************

Armed with a Graph object and a method for plotting points,
any math function that can be expressed with python can be
represented on the graph.

Let's create another blank graph to work with.

>>> import text_grapher as tg
>>> graph = tg.Graph(20, 11)
>>> graph.center_view()
>>> print(graph)
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .

Now let's try our hand at graphing a sine wave. We'll grab ``sin``
from the standard library, then iterate through the x-values in the graph
and set y equal to the sine of x. We can plot these (x, y) coordinates with
the graph's plot method.

>>> from math import sin
>>> for x in range(-10, 10):
...     y = sin(x)
...     graph.plot(x, y, '@')
...
>>> print(graph)
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
@ . . . . @ @ . . . . @ @ . . . . @ @ .
. @ . . @ . . @ . . @ . . @ . . @ . . @
. . @ @ . . . . @ @ . . . . @ @ . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .

Parametric Equations offer the ability to draw things like circles on the
graph. With these, x and y values are both functions of some other parameter,
often represented as ``t``.

We'll go back to a square graph for this one.

>>> from math import cos
>>> graph = tg.Graph(11, 11)
>>> graph.center_view()
>>> for t in range(100):
...     t *= 0.1
...     y = sin(t) * 4
...     x = cos(t) * 4
...     graph.plot(x, y, '@')
...
>>> print(graph)
. . . . . . . . . . .
. . . @ @ @ @ @ . . .
. . @ @ . . . @ @ . .
. @ @ . . . . . @ @ .
. @ . . . . . . . @ .
. @ . . . . . . . @ .
. @ . . . . . . . @ .
. @ @ . . . . . @ @ .
. . @ @ . . . @ @ . .
. . . @ @ @ @ @ . . .
. . . . . . . . . . .

That's about as close to a circle as we can get at this resolution.

When graphing parametric equations with text_grapher, it's a good idea to
overestimate the range of t values you need, and underestimate the step size.
Over-plotting like that ensures the shape is filled-in on the graph. Too few
t-values and our circle would look a bit sparse.

That sums up the basics of working with the Graph object in text_grapher, in
the next chapter you'll learn how to animate your graphs.
