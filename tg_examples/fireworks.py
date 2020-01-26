import text_grapher as tg
from math import sin, cos
from random import randint, choice

class Firework:
    chars = [
        '*WMB8&%$#@',
        'oahkbdpqwm',
        'LCJUYXZO0Q',
        'rcvunxzjft',
        '/|()1{}[]',
        '-_+<>i!lI?',
        ".'`,^:;~"
        ]

    def __init__(self, start, graph):
        self.x = randint(0, 39)
        self.y = randint(0, 39)
        self.start = start
        self.graph = graph

    def draw(self, frame):
        r = (frame - self.start) * .5
        if r > 27:
            return
        for t in range(800):
            x = r * cos(t) + self.x
            y = r * sin(t) + self.y

            # choose a lighter character as the radius increases
            ch = choice(Firework.chars[int(r/4)])
            self.graph.plot(x, y, ch)

if __name__ == '__main__':

    scene = tg.Scene()
    scene.name = 'explosions_example'
    scene.graph.background = ' '

    fireworks = []

    @scene.animate
    def fireworks_show(frame):
        if not frame % 10:
            f = Firework(frame, scene.graph)
            fireworks.append(f)

        for firework in fireworks:
            firework.draw(frame)

    scene.frame_stop = 500
    scene.render(open_player=True)
    # scene.render_gif()
