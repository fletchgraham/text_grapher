from text_grapher.graph import Graph

def test_graph():
    g = Graph()
    assert '.' in str(g)

def test_circle():
    g = Graph(11, 11)
    g.center_view()
    g.circle(0, 0, 4, '@')
    assert g.character_at(0, 4) == '@'
    assert g.character_at(4, 0) == '@'
    assert g.character_at(0, -4) == '@'
    assert g.character_at(-4, 0) == '@'
