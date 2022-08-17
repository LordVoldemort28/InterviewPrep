def cycleInGraph(input):

    noVertices = len(input)
    graph = {}

    #Insert edges
    for idx, edges in enumerate(input):
        graph[idx] = edges

    whiteSet = set()
    blackSet = set()

    for vertex in range(noVertices):
        whiteSet.add(vertex)

    while whiteSet:

        current = whiteSet.pop()

        greySet = set([current])
        stack = [current]

        while stack:
            
            currentVertex = stack.pop()
            
            for neighbor in graph[currentVertex]:
                
                if neighbor in blackSet:
                    continue
                
                if neighbor in greySet:
                    return True

                greySet.add(neighbor)
                whiteSet.remove(neighbor)
                stack.append(neighbor)
                break

        for visited in greySet:
            blackSet.add(visited)
            
    return False

def hasCycle(graph):
    
    def dfs(graph, target):

        stack = [target]
        visited = set()

        while stack:

            current = stack.pop()

            if target in graph[current]:
                return True
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return False
    
    for idx, _ in enumerate(graph):
        if dfs(graph, idx):
            return True
    return False

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [[1, 3], [2, 3, 4], [0], [], [2, 5], []],
        'output': True,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [[1,2,4], [2], [], [4], [5], [3]],
        'output': True,
        'active': True
    },
    'test_case_3': {
        'description': 'no cycle test',
        'input': [[1, 2, 3], [2], [], [4, 5], [5], []],
        'output': False,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = cycleInGraph(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
