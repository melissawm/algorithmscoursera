import sccs
import numpy as np

def run_tests(testcase, recursive=False):
    if testcase == 1:
        # This is the reverse graph from the lecture slides
        n = 9
        graph_reverse = [[1, 7], [2, 5], [3, 9], [4, 1], [5, 8], [6, 3], [6, 8], [7, 4], [7, 9], [8, 2], [9, 6]]
        graph = [arc[::-1] for arc in graph_reverse]
        # Answer: Finishing times = (7,3,1,8,2,5,9,4,6)
        # SCCs: (7,8,9,7,8,9,7,8,9)
        # Final: (3,3,3,0,0)
        realanswer = [3,3,3]
    elif testcase == 2:
        graph = [[1, 2], [2, 6], [2, 3], [2, 4], [3, 1], [3, 4], [4, 5], [5, 4], [6, 5], [6, 7], [7, 6], [7, 8], [8, 5],
                 [8, 7]]
        graph_reverse = [arc[::-1] for arc in graph]
        n = 8
        realanswer = [3,3,2]
    elif testcase == 3:
        graph = [[1, 2], [2, 3], [3, 1], [3, 4], [5, 4], [6, 4], [8, 6], [6, 7], [7, 8]]
        graph_reverse = [arc[::-1] for arc in graph]
        n = 8
        realanswer = [3,3,1,1]
    elif testcase == 4:
        graph = [[1, 2], [2, 3], [3, 1], [3, 4], [5, 4], [6, 4], [8, 6], [6, 7], [7, 8], [4, 3], [4, 6]]
        graph_reverse = [arc[::-1] for arc in graph]
        n = 8
        realanswer = [7,1]
    elif testcase == 5:
        graph = [[1, 2], [2, 3], [2, 4], [2, 5], [3, 6], [4, 5], [4, 7],
                 [5, 2], [5, 6], [5, 7], [6, 3], [6, 8], [7, 8], [7, 10],
                 [8, 7], [9, 7], [10, 9], [10, 11], [11, 12], [12, 10]]
        graph_reverse = [arc[::-1] for arc in graph]
        n = 12
        realanswer = [6,3,2,1]
    elif testcase == 6:
        with open("testcase_128.txt", "r") as infile:
            data = infile.readlines()
        graph = [list(map(int, line.rstrip(" \n").split(" "))) for line in data]
        n = 128
        graph_reverse = [arc[::-1] for arc in graph]
        realanswer = [119, 9]
    elif testcase == 7:
        with open("input_mostlyCycles_39_3200.txt", "r") as infile:
            data = infile.readlines()
        graph = [list(map(int, line.rstrip(" \n").split(" "))) for line in data]
        n = 3200
        graph_reverse = [arc[::-1] for arc in graph]
        realanswer = [2738, 240, 140, 42, 36]
    elif testcase == 8:
        with open("input_mostlyCycles_49_20000.txt", "r") as infile:
            data = infile.readlines()
        graph = [list(map(int, line.rstrip(" \n").split(" "))) for line in data]
        n = 20000
        graph_reverse = [arc[::-1] for arc in graph]
        realanswer = [11873,4625,1334,1146,576]
    elif testcase == 9:
        graph = [[1, 2], [1, 4], [2, 3], [3, 1], [5, 4]]
        n = 5
        graph_reverse = [arc[::-1] for arc in graph]
        realanswer = [3,1,1]
    elif testcase == 10:
        with open("input_mostlyCycles_5_16.txt", "r") as infile:
            data = infile.readlines()
        graph = [list(map(int, line.rstrip(" \n").split(" "))) for line in data]
        n = 16
        graph_reverse = [arc[::-1] for arc in graph]
        realanswer = [10, 3]
    elif testcase == 11:
        with open("input_mostlyCycles_65_320000.txt", "r") as infile:
            data = infile.readlines()
        graph = [list(map(int, line.rstrip(" \n").split(" "))) for line in data]
        n = 320000
        graph_reverse = [arc[::-1] for arc in graph]
        realanswer = [134344,81832,41333,30963,11028]

    graph_reverse = sorted(graph_reverse, key = lambda g: g[0])
    Grev = sccs.build_adjacency_list(graph_reverse, n)
    #print(graph_reverse)
    #print(Grev)
    leaders = list(np.zeros(n, dtype=int))
    finishing_times = list(np.zeros(n, dtype=int))
    if recursive:
        stack = [i + 1 for i in range(0, n)]
        print("  Running recursive DFS 1/2:")
        sccs.DFSLoop(Grev, n, stack, leaders, finishing_times)
        stack = [finishing_times.index(i) + 1 for i in range(n, 0, -1)]
        stack = stack[::-1]
    else:
        stack = [n]
        print("  Running iterative DFS 1/2:")
        sccs.DFSIterative(Grev, n, stack, leaders, finishing_times)
        stack = [finishing_times.index(n)+1]
    #print("  -> Finishing times: {}".format(finishing_times))

    graph = sorted(graph, key=lambda g: g[0])
    G = sccs.build_adjacency_list(graph, n)
    leaders = list(np.zeros(n, dtype=int))
    finishing_times = list(np.zeros(n, dtype=int))
    if recursive:
        print("Running recursive DFS 2/2:")
        sccs.DFSLoop(G, n, stack, leaders, finishing_times)
    else:
        print("Running iterative DFS 2/2:")
        sccs.DFSIterative(G, n, stack, leaders, finishing_times)
    #print("  -> Leaders: {}".format(leaders))

    answer = []
    for item in np.unique(leaders):
        answer.append(leaders.count(item))
    if sorted(answer, reverse=True)[0:5] == realanswer:
        print("Test {}: OK".format(testcase))
    else:
        print("Test {}: FAIL".format(testcase))
        print(realanswer)
        print(sorted(answer, reverse=True)[0:5])

if __name__ == "__main__":
    import sys, time
    #sys.setrecursionlimit(10000)
    print("Running tests...")
    #for testcase in range(1,12):
    #    run_tests(testcase)
    t = time.time()
    run_tests(11, recursive=False)
    print(time.time()-t)

    print("Done.")