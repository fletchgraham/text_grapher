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

    def __init__(self, start, x, y, graph):
        self.x = x
        self.y = y
        self.start = start
        self.graph = graph

    def draw(self, frame):
        r = (frame - self.start) * .5
        if r > 27:
            return
        for t in range(100):
            x = r * cos(t) + self.x
            y = r * sin(t) + self.y

            # choose a lighter character as the radius increases
            ch = choice(Firework.chars[int(r/4)])
            self.graph.plot(x, y, ch)

if __name__ == '__main__':

    scene = tg.Scene()
    scene.name = 'fireworks_example'
    scene.graph.background = ' '

    # make a list of fireworks to draw
    fireworks = []
    for frame in range(200):
        if not frame % 10:
            f = Firework(
                frame,
                randint(0,39),
                randint(0,39),
                scene.graph
                )
            fireworks.append(f)

    # copy fireworks and prepend so the animation loops
    prior_fireworks = [
        Firework(f.start - 200, f.x, f.y, f.graph)
        for f in fireworks
        ]

    fireworks = prior_fireworks + fireworks

    @scene.animate
    def fireworks_show(frame):
        for firework in fireworks:
            if firework.start <= frame:
                firework.draw(frame)

    scene.frame_stop = 200
    scene.render(open_player=True)
    # scene.render_gif(invert=True)
