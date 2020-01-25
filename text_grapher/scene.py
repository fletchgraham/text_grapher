"""The 3D Scene."""

import os
from text_grapher.graph import Graph
from text_grapher.player import open_graph_sequence

class Scene:
    def __init__(self, name='tg_scene'):
        self.name = name
        self.graph = Graph()
        self.frame_start = 0
        self.frame_stop = 100
        self._animations = []

    def frame(self, f):
        for a in self._animations:
            a(f)

    def animate(self, func):
        """decorator for defining animation functions"""
        self._animations.append(func)

    def render(self, open_player=False):
        for t in range(self.frame_start, self.frame_stop):
            self.graph.clear()
            self.frame(t)
            if not os.path.exists(self.name):
                os.makedirs(self.name)
            dst = os.path.join(self.name, str(t).zfill(5) + '.txt')
            with open(dst, 'w') as outfile:
                outfile.write(str(self.graph))

        if open_player:
            open_graph_sequence(self.name)
