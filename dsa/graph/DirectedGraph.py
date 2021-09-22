class Vertex(object):
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class Directed(object):

    def __init__(self):
        self.graph = {}

    def addEdge(self, source, dist, weight):

        if source not in self.graph.keys():
            self.graph[source] = []

        for vertex in self.graph[source]:
            if vertex.value == dist and vertex.weight == weight:
                print("Edge with vertex ({}, {}) and weight = {} already exist!".format(
                    source, dist, weight))
                return

        print("Added edge with vertex ({}, {}) and weight = {}".format(
            source, dist, weight))
        self.graph[source].append(Vertex(dist, weight))

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

    def DFS_Iterative(self, source):
        """
        Visit deeply in stack to find all possible path from source

        Time Complexity: O(V+E)
        Space Complexity: O(V)

        Recursive can generate stack overflow. Always perfer iterative solution
        """
        print("DFS Traversal: ", end=" ")
        visited = []
        stack = [source]

        while stack:

            current = stack.pop()
            visited.append(current)
            print(current, end=", ")

            for neighbor in self.graph[current]:
                if neighbor.value not in visited:
                    stack.append(neighbor.value)

    def BFS(self, source):
        """
        First visit neighbor.
        Graph may contain cycle so we avoid processing by adding visited array.
        Use Queue.

        Time Complexity: O(V+E)
        Space Complexity: O(V)
        """
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

    g = Directed()

    g.addEdge(0, 1, 2)
    g.addEdge(0, 2, 2)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 0, 2)
    g.addEdge(2, 0, 2)
    g.addEdge(2, 3, 2)
    g.addEdge(3, 3, 2)

    for key, value in g.graph.items():
        print("{} : ".format(key), end=" ")
        for vertex in value:
            print("{}, ".format(vertex.value), end=" ")
        print()

    g.DFS(2)
    g.BFS(2)
    g.DFS_Iterative(2)
    return


if __name__ == '__main__':
    main()
