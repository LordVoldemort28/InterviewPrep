"""
Dijkstra’s shortest path algorithm. 
This algorithm will run until all vertices in the graph have been visited.
This mean that the shortest path between any two nodes can be saved and looked up after.

Limitation: Doesn't work on negative weights

Modified by: Rahul Prajapati
Source: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
"""

"""
Pseudocode 

1. From the starting node, visited the vertex with the smallest know distance/cost
2. Once we're  moved to the lowest cost vertex, check each of its neighboring nodes
3. Calculate the distance/cost for the neighboring nodes by summing the cost of the edges
leading from the start vertex
4. If the distance/cost to a vertex we are checking is less than a know distance, update
the shortest distance from that vertex

Time complexity: O(|E| log |E| ) = O(|E| 2 log |V|) = O(|E| log |V|) with heap
"""
class Graph():

    def __init__(self, vertices, graph=None):
        self.V = vertices
        self.graph = graph

    def printSolution(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.V):
            print(node, "->", dist[node])

    def min_distance(self, dist, visited):

        min_ = float("inf")

        for v in range(self.V):

            if dist[v] < min_ and visited[v] == False:
                min_ = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        
        """
        Used to get optimal distance from src to other vertex in graph
        Time Complexity: Wikipedia: O(|E| + |V|log|V|)
                        Array: O(n^2)
                        PriorityQueue: O(E logV)
        Space Complexity: O(V + E) ---> BFS
        
        Limitation: Cannot handle -ve weights
        
        Start from distance infinity to all other vertex than source. And apply simple BFS
        with relaxation dist[v] = dist[u] + edge_weight
        """

        dist = [float("inf")] * self.V
        dist[src] = 0

        visited = [False] * self.V

        for _ in range(self.V):

            #Get next min distance
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):

                if self.graph[u][v] > 0 and \
                        visited[v] == False and \
                        dist[u] + self.graph[u][v] < dist[v]:

                    dist[v] = dist[u] + self.graph[u][v]

        return dist


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]


g.printSolution(g.dijkstra(0))
