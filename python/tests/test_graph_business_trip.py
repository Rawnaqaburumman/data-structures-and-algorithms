from code_challenges.graph_business_trip.graph_business_trip import *
import pytest

######################################################################################################


def test_graph_business1(graph_cities):

    #                           graph, [metroville, pandora,]
    actual = graph_business_trip(
        graph_cities[0], [graph_cities[3], graph_cities[1]])
    expected = "True,$82"

    assert actual == expected

# 0:graph  1:pandora  2:arendelle  3:metroville  4:monstroplolis  5:narnia  6:naboo



def test_graph_business2(graph_cities):

    #                           graph, [arendelle, monstroplolis, naboo]
    actual = graph_business_trip(
        graph_cities[0], [graph_cities[2], graph_cities[4], graph_cities[6]])
    expected = "True,$115"

    assert actual == expected

# 0:graph  1:pandora  2:arendelle  3:metroville  4:monstroplolis  5:narnia  6:naboo



def test_graph_business3(graph_cities):

    #                           graph, [naboo, pandora]
    actual = graph_business_trip(
        graph_cities[0], [graph_cities[6], graph_cities[1]])
    expected = "False,$0"

    assert actual == expected

# 0:graph  1:pandora  2:arendelle  3:metroville  4:monstroplolis  5:narnia  6:naboo


def test_graph_business4(graph_cities):

    #                           graph, [narnia, arendelle, naboo]
    actual = graph_business_trip(
        graph_cities[0], [graph_cities[5], graph_cities[2], graph_cities[6]])
    expected = "False,$0"

    assert actual == expected

# 0:graph  1:pandora  2:arendelle  3:metroville  4:monstroplolis  5:narnia  6:naboo



def test_graph_business5(graph_cities):

    #                           graph, [pandora, arendelle, monstroplolis, naboo, pandora]
    actual = graph_business_trip(
        graph_cities[0], [graph_cities[1], graph_cities[2], graph_cities[4], graph_cities[6], graph_cities[1]])
    expected = "False,$0"

    assert actual == expected

# 0:graph  1:pandora  2:arendelle  3:metroville  4:monstroplolis  5:narnia  6:naboo






@pytest.fixture
def graph_cities():
    graph = Graph()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')

    graph.add_Edge(pandora, arendelle, 150)
    graph.add_Edge(pandora, metroville, 82)

    graph.add_Edge(arendelle, pandora, 150)
    graph.add_Edge(arendelle, metroville, 99)
    graph.add_Edge(arendelle, monstroplolis, 42)

    graph.add_Edge(metroville, pandora, 82)
    graph.add_Edge(metroville, arendelle, 99)
    graph.add_Edge(metroville, monstroplolis, 105)
    graph.add_Edge(metroville, naboo, 26)
    graph.add_Edge(metroville, narnia, 37)

    graph.add_Edge(monstroplolis, arendelle, 42)
    graph.add_Edge(monstroplolis, metroville, 105)
    graph.add_Edge(monstroplolis, naboo, 73)

    graph.add_Edge(naboo, monstroplolis, 73)
    graph.add_Edge(naboo, metroville, 26)
    graph.add_Edge(naboo, narnia, 250)

    graph.add_Edge(narnia, metroville, 37)
    graph.add_Edge(narnia, naboo, 250)

# 0:graph ||| 1:pandora ||| 2:arendelle ||| 3:metroville ||| 4:monstroplolis ||| 5:narnia ||| 6:naboo
    return [graph, pandora, arendelle, metroville, monstroplolis, narnia, naboo]



