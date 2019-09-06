# The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to
# 200. The first column in the file represents the vertex label, and the particular row (other entries except the first
# column) tells all the vertices that the vertex is adjacent to. So for example, the 6th6^{th}6th row looks like :
# "6 155 56 52 120 ......".
# This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels
# 155,56,52,120,......,etc

# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above
# graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions.
# Initially, you might want to do this naively, creating a new graph from the old every time there's an edge
# contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures,
# please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you
# ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space
# provided.

from random import randint
from copy import deepcopy

if __name__ == "__main__":
    with open("kargerMinCut.txt", "r") as infile:
        data = infile.readlines()
    original_graph = [list(map(int, line.rstrip("\t\n").split("\t"))) for line in data]
    for i in range(0,len(original_graph)):
        original_graph[i][0] = [original_graph[i][0]]

    # Small test case: min_cut = 2
    # original_graph = [[[1], 2, 3],
    #          [[2], 1, 4, 5],
    #          [[3], 1, 4, 5],
    #          [[4], 2, 3, 6],
    #          [[5], 2, 3, 6],
    #          [[6], 4, 5]]

    # We will compute the total number of crossings for the final cut
    total_xings = []
    # Here you can choose how many runs of the algorithm you wish to do:
    runs = 1000
    for trial in range(0,runs):
        # Reset the graph at each run
        graph = deepcopy(original_graph)
        n = len(graph)
        while n > 2:
            # Choose two vertices to define the edge to be contracted
            # First, choose the first vertex
            v1_index = randint(0, n-1)
            v1 = graph[v1_index][0]
            # List and count the number of vertices connected to v1
            nbconnected = len(graph[v1_index])-1
            # Randomly choose second vertex from the ones connected to v1
            v2 = graph[v1_index][randint(1, nbconnected)]

            for i in range(0,n):
                if v2 in graph[i][0]:
                    v2_index = i

            # We will contract the edge (v1, v2)
            for item in graph[v2_index][0]:
                if item not in graph[v1_index][0]:
                    graph[v1_index][0].append(item)

            # Remove redundancies
            for v in graph[v2_index][1:]:
                if v not in graph[v1_index]:
                    graph[v1_index].append(v)
            for v in graph[v1_index][0]:
                if v in graph[v1_index][1:]:
                    graph[v1_index].remove(v)

            # Delete self loops (because they are stupid :)
            if v1 in graph[v1_index][1:]:
                graph[v1_index].remove(v1)
            if v2 in graph[v1_index][1:]:
                graph[v1_index].remove(v2)

            # Delete old vertex
            del graph[v2_index]
            # Recompute size to loop
            n = n-1

        # Count the number of cuts for this run and add it to the total list
        xings = max(len(graph[0])-1, len(graph[1])-1)
        total_xings.append(xings)

    print("After {} runs, MinCut has {} crossings.".format(runs, min(total_xings)))