from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjlist = defaultdict(lambda: list())
        self.weights = dict()
        self.vertices = set()
    
    def get_vertices(self):
        return list(self.vertices)
    
    def get_weight(self, src, dst):
        return self.weights[(src, dst)]
    
    def get_neighbors(self, vertex):
        return self.adjlist[vertex]
    
    def has_edge(self, src, dst):
        return dst in self.adjlist[src]
    
    def add_directed_edge(self, src, dst, weight = 0):
        self.adjlist[src].append(dst)
        self.weights[(src, dst)] = weight
        self.vertices.add(src)
        self.vertices.add(dst)
    
    def add_undirected_edge(self, src, dst, weight = 0):
        self.add_directed_edge(src, dst, weight)
        self.add_directed_edge(dst, src, weight)
    
    def remove_directed_edge(self, src, dst):
        # TODO: needs work in removing vertices
        self.adjlist[src].remove(dst)
        del self.weights[(src, dst)]
    
    def remove_undirected_edge(self, src, dst):
        self.remove_directed_edge(src, dst)
        self.remove_directed_edge(dst, src)
    