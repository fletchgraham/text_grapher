from text_grapher.util import Vector


class Scene:
    def __init__(self, name='tg_scene'):
        self._name = name
        self._objects = []
        self._camera = Camera()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value


class Entity:
    def __init__(self):
        self._location = Vector()
        self._rotation = Vector()
        self._scale = Vector(1, 1, 1)

    # LOCATION

    @property
    def location(self) -> Vector:
        return self._location

    @location.setter
    def location(self, vector):
        self._location = vector

    def translate(self, vector):
        self.location = Vector.add(self.location, vector)

    # ROTATION

    @property
    def rotation(self) -> Vector:
        return self._rotation

    @rotation.setter
    def rotation(self, vector):
        self._rotation = vector

    def rotate_x(self, radians: float):
        r = Vector(radians, 0, 0)
        self.rotation = Vector.add(self.rotation, r)

    # SCALE

    @property
    def scale_factor(self) -> Vector:
        return self._scale

    @scale_factor.setter
    def scale_factor(self, vector):
        self._scale = vector

    def scale(self, x, y, z):
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
