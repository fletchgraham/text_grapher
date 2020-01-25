"""The 3D Scene."""

from text_grapher.graph import Graph

class Scene:
    def __init__(self, name='tg_scene'):
        self.name = name
        self.graph = Graph()
        self._animations = []

    def frame(self, f):
        self.graph.clear()
        for t in range(f):
            for a in self._animations:
                a(t)

    def animate(self, func):
        """decorator for defining animation functions"""
        self._animations.append(func)

    def render(self):
        for t in range(100):
            for a in self._animations:
                a(t)
                pass
