import text_grapher as tg
from math import sin, cos

if __name__ == '__main__':

    scene = tg.Scene()
    scene.name = 'lissajous_example'

    @scene.animate
    def lissajous(frame):
        for t in range(1000):
            t *= .01
            x = cos((0 + frame)/300 * t) * 18 + 20
            y = sin(1 * t) * 18 + 20
            scene.graph.plot(x, y, u"\u2584")

    scene.frame_stop = 500
    scene.render(open_player=True)
