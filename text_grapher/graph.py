"""Essentially the rendering engine of text grapher."""

from random import choice

class Graph:
    """The canvas onto which graphics are drawn.

    The graph exists conceptually as a 2D array of characters.
    Graphics are drawn on this array by replacing the characters within its
    cells."""
    def __init__(self, width=40, height=40, character='.'):
        self._array = [[]]
        self.width = width
        self.height = height
        self.background = character
        self.clear()

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self._array])

    def clear(self):
        """Resets the graph per the settings"""
        self._array = [
            [self.background for x in range(int(self.width))]
            for y in range(int(self.height))
            ]

    def plot(self, x, y, character):
        """replace a character in the graph with the given character"""
        try:
            self._array[int(y)][int(x)] = character
        except IndexError:
            pass

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
