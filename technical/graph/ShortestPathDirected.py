# from heapq import heapify, heappop
# import __init__
# from dsa.heap.MinHeap import MinHeap

# class DistNode:
    
#     def __init__(self, id, dist):
#         self.id = id
#         self.dist = dist
        
#     def __lt__(self, node):
#         return self.dist < node.dist

def getMinEdge(dist, visited):

    minDist = float("inf")
    minNode = 0

    for idx, eachDistance in enumerate(dist):

        if eachDistance < minDist and (idx not in visited):
            minDist = eachDistance
            minNode = idx

    return minNode

def dijkstrasAlgorithm(start, edges):

    V = len(edges)

    dist = [float("inf") for _ in range(V)]
    dist[start] = 0

    visited = []

    while len(visited) <= V:

        src = getMinEdge(dist, visited)
        visited.append(src)

        for neighbor in edges[src]:

            dest, weight = neighbor

            if (dest not in visited) and dist[src] + weight < dist[dest]:
                dist[dest] = dist[src] + weight

    for idx in range(V):
        if dist[idx] == float("inf"):
            dist[idx] = -1

    return dist


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'graph': [[[1, 1], [3, 1]], [[2, 1]], [[6, 1]], [[1, 3], [2, 4], [4, 2], [5, 3], [6, 5]], [[5, 1]], [[4, 1]], [[5, 2]], [[0, 7]]],
            'start': 7
        },
        'output': [7, 8, 9, 8, 10, 11, 10, 0],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = dijkstrasAlgorithm(input['start'], input['graph'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
