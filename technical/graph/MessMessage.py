#Run bfs to reconstruct the path

def get_path(graph, src, end):

    graph_size = len(graph)
    path = {src: None}
    visited = [src]

    while len(visited) > 0:

        current = visited.pop(0)

        if current == end:
            return reconstruct_path(path, src, end)

        for neighbor in graph[current]:

            if neighbor not in path:
                visited.append(neighbor)
                path[neighbor] = current

    return None


def reconstruct_path(path, start, end):
    print(path)

    current = end
    actual_path = []

    while current:

        actual_path.append(current)
        current = path[current]

    actual_path.reverse()
    return actual_paths


graph = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'd'],
    'c': ['a', 'e'],
    'd': ['a', 'b'],
    'e': ['c'],
    'f': ['g'],
    'g': ['f'],
}
print(get_path(graph, 'a', 'e'))
