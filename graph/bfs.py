from graph import Graph

def bfs(adj, root):
    visited = set()
    visited.add(root)
    frontier = [root]
    while(frontier):
        curr = frontier.pop(0) # queue
        print(curr)
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append(neighbor)
    return 

if __name__ == "__main__":
    graph = Graph()
    graph.add_undirected_edge(0, 1)
    graph.add_undirected_edge(1, 2)
    graph.add_undirected_edge(2, 3)
    graph.add_undirected_edge(0, 4)
    graph.add_undirected_edge(1, 4)
    graph.add_undirected_edge(2, 4)
    print("BFS")
    bfs(graph.adjlist, 0)
