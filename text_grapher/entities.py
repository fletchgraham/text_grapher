"""Define Entities that can live in a 3d scene."""

from text_grapher.maths import (
    Vector,
    matrix_product,
    rotation_matrix,
    translation_matrix,
    scale_matrix,
    transformed_verts
)

class Entity:
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


class Geometry(Entity):
    def __init__(self):
        super().__init__()
        self.vertices = []
        self.edges = []
        self.character = '@'

    @property
    def world_verts(self):
        """Return the list of vertices in world space."""
        S = scale_matrix(*self.scale)
        R = rotation_matrix(*self.rotation)
        T = translation_matrix(*self.location)
        M = matrix_product(R, S)
        M = matrix_product(T, M)
        return transformed_verts(self.vertices, M)

class Cube(Geometry):
    def __init__(self, size=1):
        super().__init__()
        self.vertices = [Vector(-1.0, -1.0, -1.0),
                         Vector(+1.0, -1.0, -1.0),
                         Vector(+1.0, +1.0, -1.0),
                         Vector(-1.0, +1.0, -1.0),
                         Vector(-1.0, -1.0, +1.0),
                         Vector(+1.0, -1.0, +1.0),
                         Vector(+1.0, +1.0, +1.0),
                         Vector(-1.0, +1.0, +1.0)]

        self.vertices = [
            Vector.scale(v, size) for v
            in self.vertices
            ]

        self.edges = [(0, 4), (1, 5), (2, 6), (3, 7),
                      (0, 1), (4, 5), (7, 6), (3, 2),
                      (1, 2), (4, 7), (0, 3), (5, 6)]

class Camera(Entity):
    """The cameras main job is to provide a world_to_cam matrix"""
    def __init__(self):
        super().__init__()
        self.location = Vector(0, 0, -16)

    def world_to_cam(self, world_verts):
        """Transform the verts from world space to camera space."""
        return transformed_verts(world_verts, self.matrix)

    @property
    def matrix(self):
        """Return the matrix used to transform to camera space."""
        inverse_rotation = Vector.scale(self.rotation, -1)
        inverse_location = Vector.scale(self.location, -1)
        R = rotation_matrix(*inverse_rotation)
        T = translation_matrix(*inverse_location)

        M = matrix_product(R, T)

        return M
