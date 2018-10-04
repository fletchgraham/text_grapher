from math import sin, cos
import os

pi = 3.141
block = u' \u25A0'
identity = [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

def convert(x, y, size):
    if x > size/2 or x < -size/2:
        return -1
    else:
        x = int(round(x + size/2))
        y = int(round(y + size/2))
        return x + ((-y + size) * size + 2 * (-y + size))

def draw(graph, x, y, char):
    size = get_graph_dims(graph)
    actual = convert(x, y, size)
    for index, each in enumerate(graph):
        if index == actual and not each == "\n":
            graph[index] = char

def draw_line(graph, a, b, char):
    xa = int(round(a[0]))
    xb = int(round(b[0]))
    ya = int(round(a[1]))
    yb = int(round(b[1]))
    if xb == xa:
        for y in range(ya, yb):
            y = y
            x = xb
            draw(graph, x, y, char)
        for y in range(yb, ya):
            y = y
            x = xb
            draw(graph, x, y, char)
    else:
        m = (yb - ya)/(xb - xa)
        c = ya - m * xa
        for x in range(xa, xb):
            x = x
            y = m * x + c
            draw(graph, x, y, char)
        for x in range(xb, xa):
            x = x
            y = m * x + c
            draw(graph, x, y, char)

    if yb == ya:
        for x in range(xa, xb):
            x = x
            y = yb
            draw(graph, x, y, char)
        for x in range(xb, xa):
            x = x
            y = yb
            draw(graph, x, y, char)
    else:
        m = (xb - xa)/(yb - ya)
        c = xa - m * ya
        for y in range(ya, yb):
            y = y
            x = m * y + c
            draw(graph, x, y, char)
        for y in range(yb, ya):
            y = y
            x = m * y + c
            draw(graph, x, y, char)

def draw_connections(graph, points_list, lines_list, char):
    for i in lines_list:
        draw_line(graph, points_list[i[0]], points_list[i[1]], char)

def plot_points(graph, points_list, char):
    for i in points_list:
        x = int(round(i[0]))
        y = int(round(i[1]))
        draw(graph, x, y, char)

def matrix_product(m, n):
    # check if working with point or space
    was_matrix = True
    m_og_length = len(m)
    if type(m[0]) is not list:
        m = [m]
        was_matrix = False

    # convert make the rows in first matrix equal to columns in second
    if len(m[0]) < len(n):
        m[0].append(1.0)

    # build a blank matrix p
    p = []
    for i in range(len(m)):
        p.append([])
        for j in range(len(n)):
            p[i].append(0)

    # iterate through the rows of m
    for i in range(len(m)):
        # iterate through the columns of n
        for j in range(len(n[0])):
            # iterate through the columns of n
            for k in range(len(n)):
                p[i][j] += m[i][k] * n[k][j]

    # if m was a point rather than a space, give back a point
    # and shave off any indexes that got added
    if was_matrix is False:
        p = p[0]
        p = p[0:m_og_length]

    return p

def rotate(m=identity, rotation=[0.0, 0.0, 0.0], inverse=False):
    # use inverse to "undo" the action
    if inverse is False:
        x = rotation[0]
        y = rotation[1]
        z = rotation[2]

    else:
        x = -rotation[0]
        y = -rotation[1]
        z = -rotation[2]

    rot_x = [[1, 0, 0, 0],
             [0, cos(x), sin(x), 0],
             [0, -sin(x), cos(x), 0],
             [0, 0, 0, 1]]

    rot_y = [[cos(y), 0, -sin(y), 0],
             [0, 1, 0, 0],
             [sin(y), 0, cos(y), 0],
             [0, 0, 0, 1]]

    rot_z = [[+cos(z), +sin(z), 0, 0],
             [-sin(z), +cos(z), 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]

    p = matrix_product(m, rot_x)
    p = matrix_product(p, rot_y)
    p = matrix_product(p, rot_z)

    return p

def translate(m=identity, translation=[0.0, 0.0, 0.0], inverse=False):
    # use inverse to "undo" the action
    if inverse is False:
        x = translation[0]
        y = translation[1]
        z = translation[2]
    else:
        x = -translation[0]
        y = -translation[1]
        z = -translation[2]

    translate_m = [[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [x, y, z, 1]]

    p = matrix_product(m, translate_m)
    return p

def re_size(m=identity, s_factor=[1.0, 1.0, 1.0]):
    x = s_factor[0]
    y = s_factor[1]
    z = s_factor[2]

    scale_m = [[x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]]

    p = matrix_product(m, scale_m)
    return p

def transform_points(points_list, n):
    new_points = []
    for i in points_list:
        new_points.append(matrix_product(m=i, n=n))
    return new_points

def get_graph_dims(graph):
    graph_rows = -1
    for i in graph:
        if i == "\n":
            graph_rows += 1
    return graph_rows

def convert_to_2d(graph, points_list):
    size = get_graph_dims(graph)
    points_list_2d = []
    for i in points_list:
        canvas_point = [0, 0]
        x = i[0]
        y = i[1]
        z = i[2]
        canvas_point[0] = 5*x/z * size/2
        canvas_point[1] = 5*y/z * size/2
        points_list_2d.append(canvas_point)
    return points_list_2d

def rotate_animation(step, duration, char, draw_char, folder_name):
    t = 0
    while t <= duration:
        folder = "./"+folder_name
        if not os.path.exists(folder):
            os.makedirs(folder)
        version_num = len(os.listdir(folder))
        new_drawing = open(folder + "/graph" + str(version_num) + ".txt", "wb")

        # make blank space
        my_blank = BlankGraph(size=40, char=char)
        my_graph = my_blank.build()

        # create a camera
        my_camera = Camera(location=[0, 0, -19], rotation=[0, 0, 0])

        # create cube
        my_cube = Mesh(location=[0, 0, 0], rotation=[pi/8, t, pi/8], scale=[2, 2, 2])

        my_camera.draw(my_graph, my_cube, draw_char)

        joined = "".join(my_graph)

        new_drawing.write(bytes(joined, "UTF-8"))
        t += step

# make a blank graph class
class BlankGraph:

    def __init__(self, size=30, char=u' .'):
        self.size = size
        self.char = char

    def build(self):
        graph = []
        for y in range(0, self.size + 1):
            for x in range(0, self.size + 1):
                graph.append(self.char)
            graph.append("\n")
        return graph


# make a camera class
class Camera:
    default_location = [0.0, 0.0, 0.0]
    default_rotation = [0.0, 0.0, 0.0]
    default_fov = 1.0

    def __init__(self, location=default_location, rotation=default_rotation,
                 fov=default_fov):
        self.location = location
        self.rotation = rotation
        self.fov = fov

        matrix = translate(m=identity, translation=location, inverse=True)
        matrix = rotate(m=matrix, rotation=self.rotation, inverse=True)

        self.world_to_cam = matrix

    def draw(self, graph, mesh, char):
        # convert points to camera space - multiply mesh points by world to cam
        points_cam_space = transform_points(mesh.points, self.world_to_cam)
        # covert points to 2d
        points_2d = convert_to_2d(graph, points_cam_space)
        draw_connections(graph, points_2d, mesh.lines, char)

        # draw lines from point to point in the lines list


# make a mesh class
class Mesh:
    # define the defaults used to draw a cube
    default_points = [[-1.0, -1.0, -1.0],
                      [+1.0, -1.0, -1.0],
                      [+1.0, +1.0, -1.0],
                      [-1.0, +1.0, -1.0],
                      [-1.0, -1.0, +1.0],
                      [+1.0, -1.0, +1.0],
                      [+1.0, +1.0, +1.0],
                      [-1.0, +1.0, +1.0]]

    default_lines = [[0, 4], [1, 5], [2, 6], [3, 7],
                     [0, 1], [4, 5], [7, 6], [3, 2],
                     [1, 2], [4, 7], [0, 3], [5, 6]]

    default_location = [0.0, 0.0, 0.0]
    default_rotation = [0.0, 0.0, 0.0]
    default_scale = [1.0, 1.0, 1.0]

    # initialize
    def __init__(self, points=default_points, lines=default_lines,
                 location=default_location, rotation=default_rotation,
                 scale=default_scale):
        self.points = points
        self.lines = lines
        self.location = location
        self.rotation = rotation
        self.scale = scale

        # produce the final transform matrix by which to multiply the vertices
        matrix = re_size(m=identity, s_factor=self.scale)
        matrix = rotate(m=matrix, rotation=self.rotation)
        matrix = translate(m=matrix, translation=self.location)

        self.transform = matrix

        # create the final list of points within the init function
        self.points = transform_points(points_list=self.points, n=self.transform)

# animation class
    # will take directory, file name, duration,


def main():
    # build a blank grid
    my_blank = BlankGraph(size=44)
    my_graph = my_blank.build()

    # create a camera
    my_camera = Camera(location=[0, 0, -16], rotation=[0, 0, 0])

    # create cube
    my_cube = Mesh(location=[0,0,0], rotation=[pi/8, pi/4, pi/16], scale=[2, 2, 2])

    my_camera.draw(my_graph, my_cube, block)

    joined = "".join(my_graph)
    print(joined)

    rotate_animation(pi/64, 2*pi, "emojis_tests_01")

if __name__ == '__main__':
    main()
