from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjlist = defaultdict(lambda: list())
        self.weights = dict()
        self.vertices = defaultdict(lambda: 0) 

    def get_vertices(self):
        return list(self.vertices.keys())
    
    def get_weights(self):
        return self.weights
    
    def get_weight(self, src, dst):
        return self.weights[(src, dst)]
    
    def update_weight(self, src, dst, weight):
        if (src,dst) not in self.weights:
            raise KeyError(f"The edge {src, dst} not found.")
        self.weights[(src, dst)] = weight
    
    def get_neighbors(self, vertex):
        return self.adjlist[vertex]
    
    def has_edge(self, src, dst):
        return dst in self.adjlist[src]
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = 0
        self.adjlist[vertex] = []
    
    def add_directed_edge(self, src, dst, weight = 0):
        self.adjlist[src].append(dst)
        self.weights[(src, dst)] = weight
        self.vertices[src] += 1
        self.vertices[dst] += 1
    
    def add_undirected_edge(self, src, dst, weight = 0):
        self.add_directed_edge(src, dst, weight)
        self.add_directed_edge(dst, src, weight)
    
    def remove_directed_edge(self, src, dst, keep_vertices = False):
        if dst not in self.adjlist[src]:
            return 
        self.adjlist[src].remove(dst)
        self.vertices[src] -= 1
        self.vertices[dst] -= 1
        # delete if no edges inbound
        if self.vertices[src] == 0 and not keep_vertices:
            del self.vertices[src]
        # delete if no edges outbound
        if self.vertices[dst] == 0 and not keep_vertices:
            del self.vertices[dst]
        del self.weights[(src, dst)]
    
    def remove_undirected_edge(self, src, dst):
        self.remove_directed_edge(src, dst)
        self.remove_directed_edge(dst, src)
    
    def remove_vertex(self, vertex):
        if vertex not in self.vertices:
            return
        # delete from adjacency list
        del self.adjlist[vertex]
        for _, neighbors in self.adjlist.items():
            if vertex in neighbors:
                neighbors.remove(vertex)
        # delete from edge weights
        keys = list(self.weights.keys())
        for src, dst in keys:
            if src == vertex or dst == vertex:
                del self.weights[(src, dst)]
        # delete from vertex list
        del self.vertices[vertex]
        

    