#Time complexity -> O(VE) -> O(n^2)
def bellmenFord(edges, src, vertices):
        
    V = vertices
    
    dist = [float("inf")] * V
    dist[src] = 0

    # Relax edges V-1
    for _ in range(V-1):

        for (src, dest, weight) in edges:

            if dist[src] != float("inf") and (dist[src] + weight < dist[dest]):
                dist[dest] = dist[src] + weight

    # Relaxing once again to detect negative cycle
    # if value changes then we have a negative cycle in the graph
    # and we cannot find the shortest distances
    for (src, dest, weight) in edges:
        if dist[src] != float("Inf") and dist[src] + weight < dist[dest]:
            print("Graph contains negative weight cycle")
            return
        
    return dist

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'edges': [
                [0, 1, 2],
                [0, 2, 4],
                [1, 3, 2],
                [2, 4, 3],
                [2, 3, 4],
                [4, 3, -5]
            ],
            'src': 0,
            'vertices': 5
        },
        'output': [0, 2, 4, 2, 7],
        'active': True
    },
    'test_case_2': {
        'description': 'geek test',
        'input': {
            'edges': [
                [0, 1, -1],
                [0, 2, 4],
                [1, 2, 3],
                [1, 3, 2],
                [1, 4, 2],
                [3, 2, 5],
                [3, 1, 1],
                [4, 3, -3],
            ],
            'src': 0,
            'vertices': 5
        },
        'output': [0, -1, 2, -2, 1],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = bellmenFord(input['edges'], input['src'], input['vertices'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()


