from heapq import heapify, heappush, heappop


class Edge():

    def __init__(self, value, cost):
        self.value = value
        self.cost = cost

    def __lt__(self, edge):
        return self.cost < edge.cost


edges = [Edge(2, 3), Edge(3, 0), Edge(4, 5), Edge(5, 2), Ege(6, 6)]

print(sorted(edges)[0].cost)

heapify(edges)
heappop(edges).cost
