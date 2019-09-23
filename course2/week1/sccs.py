# The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every
# row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the
# head (recall the graph is directed, and the edges are directed from the first column vertex to the second column
# vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an
# outgoing edge to the vertex with label 47646

# Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs),
# and to run this algorithm on the given graph.

# Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes,
# separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500,
# 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds
# less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are
# 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer
# should not have any spaces in it.)

# WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may
# have to manage memory carefully. The best way to do this depends on your programming language and environment, and we
# strongly suggest that you exchange tips for doing this on the discussion forums.

import numpy as np


def build_adjacency_list(gg, n):
    Graph = [[i] for i in range(1,n+1)]
    i = 1
    k = 0
    while k < len(gg):
        if gg[k][0] == i:
            Graph[i-1].append(gg[k][1])
            k += 1
        else:
            i += 1
    #Graph = [item for item in Graph if len(item) > 1]
    return Graph


def DFSLoop(G, n, stack, leaders, finishing_times, debug=False):
    # global variable t = 0 # number of nodes processed so far/for finishing times in 1st pass
    t = 0
    # global variable s = NULL # current source vertex/ for leaders in 2nd pass
    s = 0
    # Assume nodes are labeled 1 to n.
    explored = {i+1:False for i in range(0,n)}

    # In the second pass, we have to start by checking the node with finishing time equal do n
    while stack:
        print(len(stack))
        ind = stack[-1]
        if not explored[ind]:
            s = ind
            [t, explored, stack, leaders, finishing_times] = DFS(G, ind, t, s, explored, stack, leaders, finishing_times, debug=debug)

    return finishing_times, leaders


def DFS(G, i, t, s, explored, stack, leaders, finishing_times, debug=False):
    # mark i as explored (for the rest of DFS-Loop)
    explored[i] = True
    stack.remove(i)
    leaders[i-1] = s
    tree = [arc for arc in G if arc[0] == i]
    for arc in tree:
        if not explored[arc[1]]:
            [t, explored, stack, leaders, finishing_times] = DFS(G, arc[1], t, s, explored, stack, leaders, finishing_times)
    t += 1
    finishing_times[i-1] = t
    return t, explored, stack, leaders, finishing_times

def DFSIterative(G, n, stack, leaders, finishing_times):
    #print("stack = {}".format(stack))
    explored = {i+1: False for i in range(0,n)}
    finished = {i+1: False for i in range(0,n)}
    # t accounts for the finishing times
    t = 0
    # s accounts for the leaders
    leader = stack[-1]
    while stack:
        node = stack[-1]
        #print("Current node: {}".format(node))
        #print("Current leader: {}".format(leader))
        finished[node] = True
        if not explored[node]:
            #print("This node has not yet been explored")
            explored[node] = True
            leaders[node-1] = leader
            # Start exploring
            #adj = [arc[1] for arc in G if arc[0]==node and not explored[arc[1]]]
            ########################
            # Some nodes might not have any connections in this direction
            #if node-1 is not in G[:][0]:
            #    print("node not in graph")
            #adj = [item for item in G[node-1][1:] if not explored[item]]
            adj = G[node-1][1:]
            if not adj:
                # This is a sink.
                #print("Node {} has no adjacent nodes".format(node))
                # This could be a disconnected node. We need to prune those because they are not "leaders"
                pass
            else:
                #print("Adjacent nodes: {}".format(adj))
                for adjnode in adj:
                    if not explored[adjnode]:
                        leaders[adjnode - 1] = leader
                        # Push it into the stack
                        stack.append(adjnode)
                        finished[node] = False
            if finished[node]:
                stack.pop()
        else:
            # This is the second time we have seen this node; this means that it is finished
            stack.pop()
        #print("Current leaders: {}".format(leaders))

        # We mark a node as finished if the only outgoing arcs from this node have all been explored.
        if finished[node]:
            #print("Node {} has been finished.".format(node))
            t += 1
            finishing_times[node-1] = t
            #print("f({}) = {}".format(node, t))
        #print(finished)
        #print("Current stack: {}".format(stack))
        if not stack:
            # Check if there are still unexplored nodes in the graph
            unexplored = [node for node,status in explored.items() if not status]
            if unexplored:
                # Push the first unexplored note do the stack
                #print("Pushing unexplored nodes to the stack:")
                stack.append(max(unexplored))
                #print("Current stack: {}".format(stack))
                leader = stack[-1]
    return leaders, finishing_times


if __name__ == "__main__":

    with open("SCC.txt", "r") as infile:
        data = infile.readlines()
    graph = [list(map(int, line.rstrip(" \n").split(" "))) for line in data]
    n = 875714
    graph_reverse = [arc[::-1] for arc in graph]

    recursive = False

    print("Calling DFSLoop on first graph...")
    G = graph_reverse.copy()
    leaders = list(np.zeros(n, dtype=int))
    finishing_times = list(np.zeros(n, dtype=int))
    if recursive:
        stack = [i+1 for i in range(0,n)]
        DFSLoop(G, n, stack, leaders, finishing_times)
        #print("finishing_times = {}".format(finishing_times))
        stack = [finishing_times.index(i)+1 for i in range(n,0,-1)]
        stack = stack[::-1]
    else:
        stack = [n]
        print("  Running iterative DFS 1/2:")
        DFSIterative(G, n, stack, leaders, finishing_times)
        #print("  -> Finishing times: {}".format(finishing_times))
        stack = [finishing_times.index(n)+1]

    print("Calling DFSLoop on second graph...")
    G = graph.copy()
    leaders = list(np.zeros(n, dtype=int))
    finishing_times = list(np.zeros(n, dtype=int))
    if recursive:
        DFSLoop(G, n, stack, leaders, finishing_times)
    else:
        print("Running iterative DFS 2/2:")
        DFSIterative(G, n, stack, leaders, finishing_times)

    # print("**************")
    # print("Finishing times for first (reversed) graph:")
    # print(finishing_times)
    # print("Leaders for second graph:")
    # print(np.unique(leaders))
    answer = []
    for item in np.unique(leaders):
        answer.append(leaders.count(item))
    print("*****************************")
    print("Answer: {}".format(sorted(answer, reverse=True)))
    print("*****************************")