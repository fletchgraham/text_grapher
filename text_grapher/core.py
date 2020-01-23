from text_grapher.maths import Vector

class Scene:
    def __init__(self, name='tg_scene'):
        self.name = name
        self.render_width = 40
        self.render_height = 40


class Entity:
    def __init__(self):
        self.location = Vector()
        self.rotation = Vector()
        self.scale = Vector(1, 1, 1)

    def translate(self, x=0, y=0, z=0):
        v = Vector(x, y, z)
        self.location = Vector.add(self.location, v)

    def rotate(self, x=0, y=0, z=0):
        self.rotation = Vector.add(self.rotation, Vector(x, y, z))

    def resize(self, x=1, y=1, z=1):
        _x, _y, _z = self.scale
        self.scale = Vector(x * _x, y * _y, z * _z)


class Mesh():
    def __init__(self):
        self._vertices = []
        self._edges = []


class Camera(Entity):
    def __init__(self):
        super().__init__()
        self.location = (0, 0, 10)
