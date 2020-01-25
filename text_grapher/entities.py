"""Define Entities that can live in a 3d scene."""

from text_grapher.maths import Vector


class _Entity:
    """Base class for things that live in a 3d scene.

    Objects based on this class can be transformed in 3d space."""

    def __init__(self):
        """Zero out the loc rot and scalle"""
        self.location = Vector()
        self.rotation = Vector()
        self.scale = Vector(1, 1, 1)

    def translate(self, x=0, y=0, z=0):
        """add to the location parameter of the object"""
        v = Vector(x, y, z)
        self.location = Vector.add(self.location, v)

    def rotate(self, x=0, y=0, z=0):
        """add to the rotation parameter."""
        self.rotation = Vector.add(self.rotation, Vector(x, y, z))

    def resize(self, x=1, y=1, z=1):
        """multiply scale by the given x y and z values."""
        _x, _y, _z = self.scale
        self.scale = Vector(x * _x, y * _y, z * _z)


class Mesh():
    def __init__(self):
        self._vertices = []
        self._edges = []


class Camera(_Entity):
    def __init__(self):
        super().__init__()
        self.location = (0, 0, 10)
