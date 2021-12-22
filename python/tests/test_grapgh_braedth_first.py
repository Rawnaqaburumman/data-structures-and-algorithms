from code_challenges.grapgh_breadth_first.grapgh_breadth_first import Graph,Edge,Vertex,Queue

def test_breadth_first():


    graph = Graph()

    g1 = graph.add_node(1)

    g2 = graph.add_node(2)

    g3 = graph.add_node(3)

    g4 = graph.add_node(4)

    g5 = graph.add_node(5)

    graph.add_edge(g1,g2,1)

    graph.add_edge(g1,g3,1)

    graph.add_edge(g1,g4,1)

    graph.add_edge(g1,g5,1)

    graph.add_edge(g1,g3,2)

    graph.add_edge(g2,g4,4)

    graph.add_edge(g3,g4,8)

    graph.add_edge(g3,g5,3)

    graph.add_edge(g4,g5,5)

    graph.add_edge(g5,g1,10)

    assert graph.breadth_first(g1) == [1, 2, 3, 4, 5]

    assert graph.breadth_first(g2) == [2, 4, 5, 1, 3]

    assert graph.breadth_first(g3) == [3, 4, 5, 1, 2]

    assert graph.breadth_first(g4) == [4, 5, 1, 2, 3]

    assert graph.breadth_first(g5) == [5, 1, 2, 3, 4]
