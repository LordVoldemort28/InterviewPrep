from collections import defaultdict

class Graph:

    def __init__(self, jobs):
        self.graph = self.initGraph(jobs)
        self.V = len(jobs)

    def initGraph(self, jobs):
        graph = {}
        for job in jobs:
            graph[job] = []
        return graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def getGraph(self):
        return self.graph


def topologicalSort(jobs, deps):

    graph = Graph(jobs)

    for dep in deps:
        graph.addEdge(dep[1], dep[0])

    inDegree = defaultdict(int)

    #Fill in degrees for each node
    for src in graph.getGraph():
        inDegree[src] = 0
        for neighbor in graph.getGraph()[src]:
            inDegree[neighbor] += 1

    queue = []

    #Insert node which have zero indegree
    for node in inDegree.keys():
        if inDegree[node] == 0:
            queue.append(node)

    visitedCount = 0
    topOrder = []

    while queue:

        current = queue.pop(0)
        topOrder.append(current)
        visitedCount += 1
        
        for neighbor in graph.getGraph()[current]:
            inDegree[neighbor] -= 1

            if inDegree[neighbor] == 0:
                queue.append(neighbor)

    if visitedCount != len(jobs):
        return []
    return topOrder


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'jobs': [1, 2, 3, 4],
            'deps': [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        },
        'output': [1, 4, 3, 2],
        'active': False
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'jobs': [1, 2, 3, 4, 5, 6, 7, 8],
            'deps': [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [1, 6], [1, 2], [7, 6]]
        },
        'output': [8, 5, 7, 3, 1, 4, 6, 2],
        'active': True
    }
    
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = topologicalSort(input['jobs'], input['deps'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
