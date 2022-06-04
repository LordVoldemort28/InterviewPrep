def longestPeak(array):
    pass

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3],
        'output': 6,
        'active': True
    }
}
for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = longestPeak(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
