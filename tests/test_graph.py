from text_grapher.graph import Graph

def test_graph():
    g = Graph()
    assert '.' in str(g)

def test_value_to_char():
    g = Graph()
    g.plot(0, 0, 1)
    assert g.character_at(0, 0) == '@'

def test_plot():
    g = Graph(11,11)
    g.plot(10, 10, '%')
    assert g.character_at(10, 10) == '%'

def test_circle():
    g = Graph(11, 11)
    g.center_view()
    g.circle(0, 0, 4, '@')
    assert g.character_at(0, 4) == '@'
    assert g.character_at(4, 0) == '@'
    assert g.character_at(0, -4) == '@'
    assert g.character_at(-4, 0) == '@'

def test_resize():
    g = Graph()
    g.width, g.height = 30, 30
    assert len(g._array) == 30
    assert len(g._array[0]) == 30
