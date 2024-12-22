import sys
sys.path.append("..")

from graph import Graph

def recursive_dfs(adj, root, visited):
    print(root)
    visited.add(root)
    for neighbor in adj[root]:
        if neighbor not in visited:
            recursive_dfs(adj, neighbor, visited)
    return 

def iterative_dfs(adj, root):
    visited = set()
    visited.add(root)
    frontier = [root]
    while(frontier):
        curr = frontier.pop()
        print(curr)
        for neighbor in adj[curr][::-1]: # we flip this so its the same order as recursive
            if neighbor not in visited:
                visited.add(neighbor) 
                # since we're putting things in a stack for future visits, we need to mark as visited before we go there
                # otherwise, we may "plan" to visit the same node multiple times. this isnt a problem w recursive
                # because we dont ever "plan" in recursion, we just go to a node.
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
    print("Recursive DFS")
    recursive_dfs(graph.adjlist, 0, set())
    print("Iterative DFS")
    iterative_dfs(graph.adjlist, 0)
