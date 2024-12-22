import sys
sys.path.append("..")

from graph import Graph
import heapq

def dijkstras(adjlist, weights, src, dst):
    result = -1
    pq = []
    visited = set()
    # (distance, vertex) tuples
    heapq.heappush(pq, (0, src))
    while(pq):
        dist, curr = heapq.heappop(pq)
        visited.add(curr)
        if (curr == dst):
            return dist
        for neighbor in adjlist[curr]:
            if neighbor not in visited:
                heapq.heappush(pq, (dist + weights[(curr, neighbor)], neighbor))
    return -1

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
    assert(dijkstras(graph.adjlist, graph.weights, 0, 1) == 5)
    assert(dijkstras(graph.adjlist, graph.weights, 0, 2) == 14)
    assert(dijkstras(graph.adjlist, graph.weights, 0, 6) == 30)
    print("All tests passed!")
        