import __init__
from dsa.queue.Queue import SimpleQueue
class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def assign_color(neighbors, colors):

    illegal_colors = [neighbor.color for neighbor in neighbors if neighbor.color]

    for color in colors:
        if color not in illegal_colors:
            return color


def color_graph_queue(graph, colors):

    if not graph:
        return graph

    queue = SimpleQueue()
    queue.enqueue(graph[0])

    while not queue.is_empty():

        node = queue.dequeue()

        if not node.color:
            node.color = assign_color(node.neighbors, colors)

        for neighbor in node.neighbors:

            if not neighbor.color:
                queue.enqueue(neighbor)

    return graph


def color_graph(graph, colors):

    for node in graph:

        if node in node.neighbors:
            raise Exception("Invalid graph")

        if not node.color:
            node.color = assign_color(node.neighbors, colors)

    return graph


colors = frozenset([
    'red',
    'green',
    'blue',
    'orange',
    'yellow',
    'white'
])

node_a = GraphNode('a')
node_b = GraphNode('b')
node_c = GraphNode('c')
node_d = GraphNode('d')
node_e = GraphNode('e')

node_a.neighbors.add(node_b)
node_a.neighbors.add(node_c)
node_b.neighbors.add(node_a)
node_b.neighbors.add(node_c)
node_b.neighbors.add(node_d)
node_b.neighbors.add(node_e)
node_c.neighbors.add(node_a)
node_c.neighbors.add(node_b)
node_c.neighbors.add(node_d)
node_c.neighbors.add(node_e)
node_d.neighbors.add(node_b)
node_d.neighbors.add(node_c)
node_d.neighbors.add(node_e)
node_e.neighbors.add(node_b)
node_e.neighbors.add(node_c)
node_e.neighbors.add(node_d)

graph = [node_a, node_b, node_c, node_d, node_e]
tampered_colors = list(colors)

for node in color_graph_queue(graph, tampered_colors):
    print(node.label, node.color)
