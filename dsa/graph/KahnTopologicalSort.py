from collections import defaultdict

"""
A Python program to print topological sorting of a graph using in-degree approach

Topological sorting for Directed Acyclic Graph (DAG) is a 
linear ordering of vertices such that for every directed edge u v, 
vertex u comes before v in the ordering. Topological Sorting for a 
graph is not possible if the graph is not a DAG.

Limitions:

    1. Sorting only works with graph that are directed and acyclic graph(DAC).
    2. There is at least one vertex in the "graph" with an "in-degree" of 0. 
        If all vertices in the graph have non-zero "in-degree" then graph does not have
        a starting point and directed edges has a cycle.

Modified by: Rahul Prajapati
Source: https://www.geeksforgeeks.org/topological-sorting/
""" 

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # The function to do Topological Sort.

    def topologicalSort(self):
        
        """        
        Dependency chart sorting
        
        Time Complexity: O(V+E)
        Space Complexity: O(V+E)
        
        Uses InDegree and OutDegree Method
        
        First calculate InDegree of all vertex then negate as you visit them
        by using queue
        
        Note:
        * If nodes represent same parent before n-1 then subgraph
        has a cycle.
        * If counter is above size of vertices then cycle exist
        * If starting InDegree is not zero then sorting is not possible
        because there's not a starting node
        """

        #Initialize all in-degrees as 0.
        in_degree = [0]*(self.V)

        # Traverse adjacency lists to fill in-degrees of
        # vertices based on upcoming directed edges.
        # This step takes O(V + E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with in-degree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        visited_count = 0

        # List to store top order
        top_order = []

        while queue:

            # Dequeue vertex which 0 in-degree
            u = queue.pop(0)
            top_order.append(u)

            # Adjust in-degree based on current vertex
            for i in self.graph[u]:
                in_degree[i] -= 1
                
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            visited_count += 1

        # Check if there was a cycle
        if visited_count != self.V:
            print("There exists a cycle in the graph")
        else:
            # Print topological order
            print(top_order)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topologicalSort()
