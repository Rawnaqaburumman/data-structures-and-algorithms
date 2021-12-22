from collections import deque

class Queue():


  def __init__(self):

    self.dq = deque()

  def enqueue(self,value):

    self.dq.appendleft(value)

  def dequeue(self):

    return self.dq.pop()

  def __len__ (self):


    return len(self.dq)

class Vertex:

    def __init__(self,value):
        self.value=value

    def __str__(self):

        return str(self.value)

class Edge:

    def __init__(self,vertex,weight):

        self.vertex = vertex
        self.weight = weight

class Graph:

    def __init__(self) -> None:
        self._adj_list={}

    def add_node(self,value):

        node=Vertex(value)
        self._adj_list[node]=[]

        return node

    def add_edge(self,start_vertex,end_vertex,weight =0):

        if start_vertex not in self._adj_list:

            raise KeyError('Start vertex not found in the graph')

        if end_vertex not in self._adj_list:

            raise KeyError('end vertex not found in the graph')
        edge=Edge(end_vertex,weight)
        self._adj_list[start_vertex].append(edge)

    def get_neighbors(self,vertex):
        # return self._adj_list.get(vertex,[])
        return self._adj_list[vertex]

    def get_nodes(self):

        return self._adj_list.keys()

    def size(self):

        return len(self._adj_list)

    ## code challenge 36

    def breadth_first(self,start_vertex):

        queue=Queue()
        visited=set()
        result=[]
        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)
        if start_vertex==None:
            return "It is an empty graph"
        while len(queue):
            current_vertex = queue.dequeue()

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor.value)

        return result



if __name__=="__main__":

    # val1=graph.add_node("A")
    # val2=graph.add_node("B")
    # val3=graph.add_node("C")
    # graph.add_edge(val1,val2,50)
    # graph.add_edge(val1,val3,1)
    # graph.add_edge(val2,val3,1)
    graph=Graph()
    g1 = graph.add_node(1)
    g2 = graph.add_node(2)
    g3 = graph.add_node(3)
    g4 = graph.add_node(4)
    g5 = graph.add_node(5)
    g6 = graph.add_node(6)
    graph.add_edge(g1,g2,1)
    # graph.add_edge(g2,g1,1)
    # graph.add_edge(g3,g1,1)
    # graph.add_edge(g4,g1,1)
    # graph.add_edge(g5,g1,1)
    graph.add_edge(g2,g1,1)
    graph.add_edge(g2,g3,1)
    graph.add_edge(g3,g2,1)
    graph.add_edge(g3,g4,1)
    graph.add_edge(g4,g3,2)

    graph.add_edge(g4,g5,4)

    graph.add_edge(g5,g6,8)

    graph.add_edge(g6,g5,3)

    # graph.add_edge(g4,g5,5)

    # graph.add_edge(g5,g1,10)
    print(graph.breadth_first(g2))
    