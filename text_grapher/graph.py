"""Essentially the rendering engine of text grapher."""

from math import sin, cos
from random import choice

class Graph:
    """The canvas onto which graphics are drawn.

    The graph exists conceptually as a 2D array of characters.
    Graphics are drawn on this array by replacing the characters within its
    cells."""
    def __init__(self, width=40, height=40, character='.'):
        self._array = [[]]
        self._width = width
        self._height = height
        self.background = character
        self.clear()

        self.offset_x = 0
        self.offset_y = 0
        self.scale_x = 1
        self.scale_y = 1

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self._array])

    def character_at(self, x, y):
        """Return the character at the given coordinates"""

        x = int(self.scale_x * x + self.offset_x)

        # if the point is off either side of the grapher, get out early
        if x > self.width - 1 or x < 0:
            return None

        y = int(self.scale_y * y + self.offset_y)

        # if the point is off the top or bottom, get out early
        if y > self.height - 1 or y < 0:
            return None

        return self._array[y][x]

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value
        self.clear()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value
        self.clear()

    def center_view(self):
        """place the origin at the center and flip y axis"""
        self.offset_x = self.width / 2
        self.offset_y = self.height / 2
        self.scale_y = -1

    def clear(self):
        """Resets the graph per the settings"""
        self._array = [
            [self.background for x in range(int(self.width))]
            for y in range(int(self.height))
            ]

    def plot(self, x, y, character):
        """replace a character in the graph with the given character"""
        x = int(self.scale_x * x + self.offset_x)

        # if the point is off either side of the grapher, get out early
        if x > self.width - 1  or x < 0:
            return

        y = int(self.scale_y * y + self.offset_y)

        # if the point is off the top or bottom, get out early
        if y > self.height - 1 or y < 0:
            return

        self._array[y][x] = character


    def line(self, x1, y1, x2, y2, character):
        """draw a line from (x1, y1) to (x2, y2) using the given character"""
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        dx = x2 - x1
        dy = y2 - y1

        # graph the line once in terms of x
        for x in range(min(x1, x2), max(x1, x2)):
            y = (dy / dx) * (x - x1) + y1
            self.plot(x, y, character)

        # and again in terms of y so that vertical lines can be drawn
        for y in range(min(y1, y2), max(y1, y2)):
            x = (dx / dy) * (y - y1) + x1
            self.plot(x, y, character)

    def circle(self, x, y, radius, character):
        """Draw a circle on the graph at (x, y) with the given radius and char.
        """

        for t in range(100):
            t *= .1
            _y = sin(t) * radius + y
            _x = cos(t) * radius + x
            self.plot(_x, _y, character)

    @classmethod
    def random_char(self, density=7):
        """Return a random character of the given density.

        On a white background, a denser character will appear darker.
        """
        if density > 7:
            density = 7
        if density < 0:
            density = 0

        # a list of characters ordered by denisty
        chars = [
            ' ',
            ".'`,^:;~",
            '-_+<>i!lI?',
            '/|()1{}[]',
            'rcvunxzjft',
            'LCJUYXZO0Q',
            'oahkbdpqwm',
            '*WMB8&%$#@',
            ]

        return choice(chars[density])
