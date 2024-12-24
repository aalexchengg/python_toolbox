# author: abcheng

import sys
sys.path.append("..")

from graph import Graph
import heapq

# complexity is O((v + e)log v)

def dijkstras(graph: Graph, src):
    num_vertices = len(graph.get_vertices())
    pq = []
    visited = set()
    distance_matrix = dict()
    # (distance, vertex) tuples
    heapq.heappush(pq, (0, src))
    while(pq and len(distance_matrix) < num_vertices):
        dist, curr = heapq.heappop(pq)
        visited.add(curr)
        distance_matrix[curr] = dist
        for neighbor in graph.get_neighbors(curr):
            if neighbor not in visited:
                heapq.heappush(pq, (dist + graph.get_weight(curr, neighbor), neighbor))
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
    matrix = dijkstras(graph, 0)
    assert(matrix[1] == 5)
    assert(matrix[2] == 14)
    assert(matrix[6] == 30)
    print("All tests passed!")
        