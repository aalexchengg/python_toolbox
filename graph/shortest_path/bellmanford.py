# author: abcheng

import sys
sys.path.append("..")

from graph import Graph

# complexity is O(VE)

def bellman_ford(adjlist, weights, src):
    # set up the distance matrix
    vertices = list(adjlist.keys())
    distance_matrix = dict()
    for vertex in vertices:
        distance_matrix[vertex] = float('inf')
    distance_matrix[src] = 0
    # relaxtion phase V times, check if last iteration creates a cycle.
    for i in range(len(vertices)):
        # go through every edge
        for edge, weight in weights.items():
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
                