#Time complexity: O(n) 
#Space complexity: O(n)
def maxSubsetNoAdjacent(array):
    
    if len(array) < 1:
        return 0
    
    if len(array) < 2:
        return array[-1]
    
    maxSum = array.copy()
    maxSum[1] = max(array[0], array[1])

    for idx in range(2, len(array)):
        maxSum[idx] = max(
            (maxSum[idx-2]+array[idx]),
            maxSum[idx-1]
        )

    return maxSum[-1]

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': [75, 105, 120, 75, 90, 135],
        'output': 330,
        'active': True
    },
    'test_case_2': {
        'description': 'normal test',
        'input': [],
        'output': 0,
        'active': True
    },
    'test_case_3': {
        'description': 'normal test',
        'input': [105, 70],
        'output': 105,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = maxSubsetNoAdjacent(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
