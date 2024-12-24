# author: abcheng

import sys
sys.path.append("..")

from graph import Graph

# complexity is O(VE)

def bellman_ford(graph: Graph,  src):
    # set up the distance matrix
    vertices = graph.get_vertices()
    distance_matrix = dict()
    for vertex in vertices:
        distance_matrix[vertex] = float('inf')
    distance_matrix[src] = 0
    # relaxtion phase V times, check if last iteration creates a cycle.
    for i in range(len(vertices)):
        # go through every edge
        for edge, weight in graph.get_weights().items():
            a, b = edge
            # source cant be infinity, and it needs to improve distance to destination
            if distance_matrix[a] != float('inf') and distance_matrix[a] + weight < distance_matrix[b]:
                # if a weight is still being updated, and we're on the Vth relaxation, we've found
                # a negative weight cycle
                if i == len(vertices) - 1 :
                    # return an empty dictionary
                    return dict()
                # update the new shortest distance distance
                distance_matrix[b] = distance_matrix[a] + weight
    return distance_matrix

if __name__ == "__main__":
    graph = Graph()
    graph.add_directed_edge(0, 1, 5)
    graph.add_directed_edge(0, 2, 14)
    graph.add_directed_edge(1, 3, 3)
    graph.add_directed_edge(3, 4, 9)
    graph.add_directed_edge(3, 5, 12)
    graph.add_directed_edge(5, 6, 14)
    graph.add_directed_edge(4, 6, 13)
    graph.add_directed_edge(4, 7, 14)
    graph.add_directed_edge(7, 6, 16)
    graph.add_directed_edge(2, 7, 16)
    graph.add_directed_edge(2, 8, 5)
    graph.add_directed_edge(8, 7, 10)
    matrix = bellman_ford(graph, 0)
    assert(matrix[1] == 5)
    assert(matrix[2] == 14)
    assert(matrix[6] == 30)

    graph2 = Graph()
    graph2.add_directed_edge(0, 1, 5)
    graph2.add_directed_edge(1, 2, 1)
    graph2.add_directed_edge(1, 3, 2)
    graph2.add_directed_edge(2, 4, 1)
    graph2.add_directed_edge(4, 3, -1)
    matrix = bellman_ford(graph2, 0)
    assert(matrix[1] == 5)
    assert(matrix[2] == 6)
    assert(matrix[3] == 6)
    assert(matrix[4] == 7)
    print("All tests passed!")