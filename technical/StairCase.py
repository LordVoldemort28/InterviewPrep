def staircaseTraversal(height, maxSteps):
    # Write your code here.

    def dfs(n, way=0):

        if n == 0:
            way += 1
        elif n > 0:
            for i in range(1, (maxSteps+1)):
                way += dfs(n-i)
        return way

    return dfs(height)

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': {
            'height': 4,
            'maxSteps': 2
            },
        'output': 5,
        'active': True
    },
    'test_case_2': {
        'description': 'only one way test',
        'input': {
            'height': 4,
            'maxSteps': 1
        },
        'output': 1,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = staircaseTraversal(input['height'], input['maxSteps'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
