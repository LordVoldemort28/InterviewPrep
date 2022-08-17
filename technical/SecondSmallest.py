def secondSmallestSorted(arr):
    if len(arr) < 2:
        return None
    return sorted(arr)[1]

def secondSmallest(arr):
    
    if len(arr) < 2:
        return None
    
    first, second = (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    for idx in range(2, len(arr)):
        if arr[idx] < first:
            first = arr[idx]
        if arr[idx] < second and second > first:
            second = arr[idx]
    
    return second

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [0],
        'output': None,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [0, 1],
        'output': 1,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': [2, -1, 0, 10],
        'output': 0,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = secondSmallest(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
