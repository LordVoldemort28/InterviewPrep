def getMin(dist, visited):
    
    min_ = float("inf")
    minIndex = 0
    
    for idx, eachDistance in enumerate(dist):
        
        if eachDistance < min_ and (idx not in visited):
            minIndex = idx
            min_ = eachDistance
    return minIndex
        
def printPath(pathTraveled, trainStationName, target):
    
    path = []
    current = target
    
    while current != '':
        
        path.append(current)
        current = pathTraveled[current]
    
    path = [trainStationName[station] for station in reversed(path)]
    
    return '->'.join(path)

def getShortestPath(graph, trainStationName, src, target):
    
    vertices = len(graph)
    dist = [float("inf")] * vertices
    pathTraveled = {}
    
    dist[src] = 0
    pathTraveled[src] = ''
    
    visited = []
    
    while len(visited) <= vertices:
        
        vertex = getMin(dist, visited)
        visited.append(vertex)
        
        for neighbor in graph[vertex]:
            
            if (neighbor is not visited) and \
                dist[vertex] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[vertex] + 1
                    pathTraveled[neighbor] = vertex

    if dist[target] == float('inf'):
        return 'Not possible'
    
    return printPath(pathTraveled, trainStationName, target)

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'connections': {
                0: [1, 4, 6],
                1: [0, 2],
                2: [1, 3],
                3: [2, 10, 5],
                4: [0, 5],
                5: [4, 3],
                6: [0, 7],
                7: [6, 8],
                8: [7, 9],
                9: [10, 8],
                10: [3, 9]
            },
            'trainStationName': {
                0: 'King\'s Cross St Pancras',
                1: 'Angel',
                2: 'Old street',
                3: 'Moorgate',
                4: 'Farringdon',
                5: 'Barbican',
                6: 'Russell Square',
                7: 'Holborn',
                8: 'Chancery Lane',
                9: 'St Paul\' s',
                10: 'Bank'
            },
            'src': 0,
            'dest': 9
        },
        'output': 'King\'s Cross St Pancras->Russell Square->Holborn->Chancery Lane->St Paul\' s',
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = getShortestPath(input['connections'], input['trainStationName'], input['src'], input['dest'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
