import os
import text_grapher as tg

graph = tg.Graph()

graph.width = 64
graph.height = 64

graph.load_image(os.path.join('img', 'statue.jpg'))

print(graph)
