"""The 3D Scene."""

import os
from text_grapher.graph import Graph
from text_grapher.player import open_graph_sequence
from text_grapher.entities import Camera, Geometry

class Scene:
    def __init__(self, name='tg_scene'):
        self.name = name
        self.graph = Graph()
        self.frame_start = 0
        self.frame_stop = 250
        self._animations = []
        self.geometries = []
        self.camera = Camera()

    def add(self, geometry):
        self.geometries.append(geometry)

    def frame(self, f):
        self.graph.clear()
        for a in self._animations:
            a(f)

        for geometry in self.geometries:
            self.draw_geometry(geometry)

    def convert_verts_to_2d(self, verts_list):
        size = self.graph.width
        points_list_2d = []
        for v in verts_list:
            x = 5*v.x/v.z * size/2
            y = 5*v.y/v.z * size/2
            points_list_2d.append((x, y))
        return points_list_2d

    def draw_geometry(self, geometry):
        """draw the geometry on the graph"""

        world_verts = geometry.world_verts
        cam_verts = self.camera.world_to_cam(world_verts)
        points = self.convert_verts_to_2d(cam_verts)
        for segment in geometry.edges:
            A = points[segment[0]]
            B = points[segment[1]]
            self.graph.line(*A, *B, geometry.character)

    def animation(self, func):
        """decorator for defining animation functions"""
        self._animations.append(func)

    def render_gif(self, invert=False):
        # import here so the rest of the package is usable without pillow
        from PIL import Image, ImageDraw
        spacing = 1.1

        imgs = []

        background_color = 255
        text_color = 0
        if invert:
            background_color, text_color = 0, 255

        for t in range(self.frame_start, self.frame_stop):
            self.frame(t)
            graph = str(self.graph)
            width = int(self.graph.width * 12 + 15)
            height = int(self.graph.height * 12 + 15)

            img = Image.new(
                'L',
                (width, height),
                color = background_color
                )

            d = ImageDraw.Draw(img)
            d.text(
                (10,10),
                graph,
                fill=text_color,
                spacing=1.0
                )

            imgs.append(img)

        imgs[0].save(
            f'{self.name}.gif',
            save_all=True,
            append_images=imgs[1:],
            duration=33,
            loop=0)


    def render(self, open_player=False):

        for t in range(self.frame_start, self.frame_stop):
            self.frame(t)
            if not os.path.exists(self.name):
                os.makedirs(self.name)
            dst = os.path.join(self.name, str(t).zfill(5) + '.txt')
            with open(dst, 'w') as outfile:
                outfile.write(str(self.graph))

        if open_player:
            open_graph_sequence(self.name)
