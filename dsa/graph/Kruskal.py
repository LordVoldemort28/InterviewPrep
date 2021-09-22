import heapq

"""
Modified by: Rahul Prajapati
Source: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
"""
class DisjointSet:

    def __init__(self):
        self.parent = {}

    def makeSet(self, universe):

        for i in range(0, universe):
            self.parent[i] = i

    def find(self, x):

        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def optimized_path_compression(self, x):
        #Time complexity: O(logN)
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):

        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot != yRoot:
            self.parent[xRoot] = yRoot

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class MinHeap(object):

    def __init__(self, heap=[]):
        self.heap = heap
        heapq.heapify(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if not len(self):
            return None

        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)
    
    
class Edge:

    def __init__(self, src, dist, weight):
        self.src = src
        self.dist = dist
        self.weight = weight

    def __lt__(self, edge):
        return self.weight < edge.weight

    def __str__(self):
        return "(src={}, dist={}, weight={})".format(self.src, self.dist, self.weight)


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append(Edge(u, v, w))

    def kruskal(self):
        """
        Pick all minimum edges until it doesn't make cycle
        then connect them all.
        
        Time Complexity: 
                        Heap -> O(E logE) 
                        Array -> O(|V||E|) -> O(n^2)
        Space complexity: O(V)
        """
        #This will store the resultant MST
        result = []
        
        minimumCost = 0

        min_edges = MinHeap(self.graph)

        djs = DisjointSet()
        djs.makeSet(self.V)

        for _ in range(self.V):

            c_edge = min_edges.pop()
            src, dist, weight = c_edge.src, c_edge.dist, c_edge.weight

            if not djs.connected(src, dist):
                
                result.append(c_edge)
                minimumCost += weight
                djs.union(src, dist)

        for edge in result:
            print("%d -- %d == %d" % (edge.src, edge.dist, edge.weight))

        print("Minimum Spanning Tree", minimumCost)


g = Graph(4)

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kruskal()
