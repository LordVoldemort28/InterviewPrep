from collections import defaultdict


def getPairsCount(arr, n, sum):

    m = defaultdict(int)

    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1

    twice_count = 0

    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):

        twice_count += m[sum - arr[i]]

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twice_count
    return int(twice_count / 2)


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'arr': [1, 5, 7, -1, 5],
            'target': 6
        },
        'output': 3,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'arr': [1, 1, 1, 1],
            'target': 2
        },
        'output': 6,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': {
            'arr': [100, 10, 3, 2, 8, 9],
            'target': 12
        },
        'output': 2,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = getPairsCount(input['arr'], len(input['arr']), input['target'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
