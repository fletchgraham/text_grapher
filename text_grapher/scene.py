"""The 3D Scene."""

import os
from text_grapher.graph import Graph

class Scene:
    def __init__(self, name='tg_scene'):
        self.name = name
        self.graph = Graph()
        self._animations = []

    def frame(self, f):
        for t in range(f):
            for a in self._animations:
                a(t)

    def animate(self, func):
        """decorator for defining animation functions"""
        self._animations.append(func)

    def render(self):
        for t in range(10):
            self.frame(t)
            if not os.path.exists(self.name):
                os.makedirs(self.name)
            dst = os.path.join(self.name, str(t).zfill(5) + '.txt')
            with open(dst, 'w') as outfile:
                outfile.write(str(self.graph))
