"""
Forex Exchange

- A list of foreign exchange rates
- A selected currency
- A target currency

Your goal is to calculate the max amount of 
the target currency to 1 unit of the selected
currency through the FX transactions.
Assume all transactions are free and done immediately.
If you cannot finish the exchange, return -1.0

Using modified bellmen ford algorithm
"""
def findArbitrage(nodes, edges, start, target):
    
    V = len(nodes)
    dist = [float("-inf")] * V
    dist[start] = 1
    
    for _ in range(V-1):
        
        for (src, dest, rate) in edges:
            
            if dist[src] != float("-inf") and dist[src] * rate > dist[dest]:
                dist[dest] = dist[src] * rate
    
    for (src, dest, rate) in edges:

        if dist[src] != float("-inf") and dist[src] * rate > dist[dest]:
            print('Negative cycle detected')

    print("{} to {} --> {}".format(nodes[start], nodes[target], dist[target]))
    
    return dist[target] if dist[target] != float("-inf") else -1.0

test_cases = {
    'test_case_1': {
        'description': 'three country test',
        'input': {
            'nodes': {
                0: 'USD',
                1: 'JPY',
                2: 'GBP'
            },
            'edges': [
                [0, 1, 109],
                [0, 2, 0.71],
                [2, 1, 155]
            ],
            'src': 0,
            'target': 1
        },
        'output': 110.05,
        'active': True
    },
    'test_case_2': {
        'description': 'four test',
        'input': {
            'nodes': {
                0: 'USD',
                1: 'CAD',
                2: 'GBP',
                3: 'JPY'
            },
            'edges': [
                [0, 1, 1.3],
                [0, 2, 0.71],
                [0, 3, 109],
                [2, 3, 155]
            ],
            'src': 0,
            'target': 3
        },
        'output': 110.05,
        'active': True
    },
    'test_case_3': {
        'description': 'not possible test',
        'input': {
            'nodes': {
                0: 'USD',
                1: 'CAD',
                2: 'GBP',
                3: 'JPY',
                4: 'KRW',
                5: 'CNY'
            },
            'edges': [
                [0, 2, 0.7],
                [0, 3, 109],
                [2, 3, 155],
                [1, 5, 5.27],
                [1, 4, 921]
            ],
            'src': 0,
            'target': 5
        },
        'output': -1.0,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = findArbitrage(input['nodes'], input['edges'], input['src'], input['target'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
