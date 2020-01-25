"""The 3D Scene."""

from text_grapher.graph import Graph

class Scene:
    def __init__(self, name='tg_scene'):
        self.name = name
        self.render_width = 40
        self.render_height = 40
        self.background = '.'
        self._animations = []

    def graph_array(self, f):
        for a in self._animations:
            a(f)
        graph = Graph(
            self.render_width,
            self.render_height,
            self.background,
            )
        return graph._array

    def animate(self, func):
        """decorator for defining animation functions"""
        self._animations.append(func)
