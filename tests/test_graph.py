from text_grapher.graph import Graph

def test_graph():
    g = Graph()
    assert '.' in str(g)
