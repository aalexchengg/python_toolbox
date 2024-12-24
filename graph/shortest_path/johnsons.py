import sys
import bellmanford
import dijkstras
sys.path.append("..")

from graph import Graph

# Complexity is O((V(V+E)logV + VE) (dijkstras V times + bellman ford)

def johnsons(graph: Graph):
    # first, add a source vertex and an edge to each vertex
    vertices = graph.get_vertices()
    source = -1
    for vertex in vertices:
        graph.add_directed_edge(source, vertex, 0)
    # get the shortest distance from our source vertex to every other vertex
    # using bellman ford
    matrix = bellmanford.bellman_ford(graph, source)
    # remove the vertex
    graph.remove_vertex(source)
    # reweight all the edges such that 
    # weight(u,v) = weight(u,v) + matrix[u] - matrix[v]
    for (u,v) in graph.get_weights().keys():
        new_weight = graph.get_weight(u, v) + matrix[u] - matrix[v]
        graph.update_weight(u, v, new_weight)
    # now that all the weights are positive, use Dijkstra's to find shortest path
    result = dict()
    for vertex in vertices:
        result[vertex] = dijkstras.dijkstras(graph, vertex)
    return result

if __name__ == "__main__":
    graph = Graph()
    


    