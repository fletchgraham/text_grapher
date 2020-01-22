from text_grapher.util import Vector


class Scene:
    def __init__(self):
        self.frame_start = 1
        self.frame_stop = 1
        self.meshes = []
        self.camera = Camera()

    def render(self):
        print('render not implemented!')

    def show(self, frame):
        print('show not implemented')


class Object3D:
    def __init__(self):
        self._location = Vector()
        self._rotation = Vector()
        self._scale = Vector(1, 1, 1)

    # LOCATION

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, vector):
        self._location = vector

    def translate(self, vector):
        self._location = vector_add(self.location, vector)

    # ROTATION

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, vector):
        self._rotation = vector

    def rotate(self, vector):
        self._rotation = vector_add(self.rotation, vector)

    # SCALE

    @property
    def scale_factor(self):
        return self._scale

    @scale_factor.setter
    def scale_factor(self, vector):
        self._scale = vector

    def scale(self, vector):
        self._scale = vector_add(self.scale_factor, vector)


class Mesh(Object3D):
    def __init__(self):
        super().__init__()
        self.vertices = []
        self.edges = []
        self.character = 'M'


class Camera(Object3D):
    def __init__(self):
        super().__init__()
        self.location = (0, 0, 10)
