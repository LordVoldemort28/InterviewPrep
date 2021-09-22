#Goal: Always selected smallest edge from know vertices

"""
Modified by: Rahul Prajapati
Source: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
"""
class Vertex(object):

    def __init__(self, src, dist, weight):
        self.src = src
        self.dist = dist
        self.weight = weight

    def __lt__(self, vertex):
        return self.weight < vertex.weight


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def addEdge(self, source, dist, weight):

        if source not in self.graph.keys():
            self.graph[source] = []

        if dist not in self.graph.keys():
            self.graph[dist] = []

        self.graph[source].append(Vertex(source, dist, weight))
        self.graph[dist].append(Vertex(dist, source, weight))

    def get_all_egdes(self):

        edges = []

        for key in self.graph.keys():
            for edge in self.graph[key]:
                edges.append(edge)

        return sorted(edges)

    def prims(self):
        """
        Prims algorithm to find minimum spanning tree.
        Always select smallest edge from know vertices till every vertex is explored
        
        Time complexity: O(E logV)
        Space complexity: O(V)
        
        Limitation: List of edges has to be searched from begining as new edge gets added
        """
        edges = self.get_all_egdes()

        first_min_edge = edges.pop(0)
        src, dist, weight = first_min_edge.src, first_min_edge.dist, first_min_edge.weight

        result = [first_min_edge]
        minimum_cost = weight
        explored_vertices = set([src, dist])

        while len(explored_vertices) < self.V:

            for idx, edge in enumerate(edges):

                src, dist, weight = edge.src, edge.dist, edge.weight

                if (src in explored_vertices) != (dist in explored_vertices):

                    #Update explored vertices
                    explored_vertices.add(src)
                    explored_vertices.add(dist)

                    #Add result
                    result.append(edge)

                    #Minimum
                    minimum_cost += weight

                    #pop the edge
                    edges.pop(idx)

                    break

        for edge in result:
            print("%d -- %d == %d" % (edge.src, edge.dist, edge.weight))

        print("Minimum Spanning Tree", minimum_cost)


g = Graph(3)
g.addEdge(1, 2, 3)
g.addEdge(0, 2, 2)
g.addEdge(0, 1, 4)

g.prims()
print()
g = Graph(7)

g.addEdge(0, 1, 28)
g.addEdge(0, 5, 10)
g.addEdge(1, 2, 16)
g.addEdge(1, 6, 14)
g.addEdge(2, 3, 12)
g.addEdge(3, 4, 22)
g.addEdge(6, 3, 18)
g.addEdge(6, 4, 24)
g.addEdge(4, 5, 25)

g.prims()
print()
g = Graph(4)

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.prims()
print()
