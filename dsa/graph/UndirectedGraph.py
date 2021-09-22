"""
Written by: Rahul Prajapati
"""

class Vertex(object):

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class UndirectedGraph(object):

    def __init__(self):
        self.graph = {}

    def addEdge(self, source, dist, weight):

        if source not in self.graph.keys():
            self.graph[source] = []

        if dist not in self.graph.keys():
            self.graph[dist] = []

        for vertex in self.graph[source]:
            if vertex.value == dist and vertex.weight == weight:
                print("Edge with vertex ({}, {}) and weight = {} already exist".format(
                    source, dist, weight))
                return

        for vertex in self.graph[dist]:
            if vertex.value == source and vertex.weight == weight:
                print("Edge with vertex ({}, {}) and weight = {} already exist".format(
                    source, dist, weight))
                return

        self.graph[source].append(Vertex(dist, weight))
        self.graph[dist].append(Vertex(source, weight))
        print("Added edge with vertex ({}, {}) and weight = {}".format(
            source, dist, weight))

    def DFS(self, source):
        print("DFS Traversal: ", end=" ")
        visited = []
        
        self.DFSUtils(source, visited)
    
    def DFSUtils(self, v, visited):
        
        visited.append(v)
        print(v, end=", ")
        
        for neighbor in self.graph[v]:
            if neighbor.value not in visited:
                self.DFSUtils(neighbor.value, visited)

    def BFS(self, source):
        print("BFS Traversal: ", end=" ")
        queue = [source]
        visited = [source]
        
        while queue:
            
            s = queue.pop(0)
            print(s, end=" ")
            
            for neighbor in self.graph[s]:
                if neighbor.value not in visited:
                    queue.append(neighbor.value)
                    visited.append(neighbor.value)

def main():
    g = UndirectedGraph()

    g.addEdge(0, 1, 1)
    g.addEdge(0, 2, 1)
    g.addEdge(3, 4, 1)
    g.addEdge(3, 2, 1)
    g.addEdge(2, 8, 1)
    g.addEdge(4, 6, 1)
    g.addEdge(6, 7, 1)
    g.addEdge(3, 5, 1)

    for key, value in g.graph.items():
        print("{} : ".format(key), end=" ")
        for vertex in value:
            print("{}, ".format(vertex.value), end=" ")
        print()
        
    g.DFS(2)
    print()
    g.BFS(0)

    return


if __name__ == '__main__':
    main()
