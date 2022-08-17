def sortStack(stack):
    
    if len(stack) <= 1:
        return stack
    
    one = stack.pop()
    sortStack(stack)
    two = stack.pop()
    
    smallerValue = one if one < two else two
    largerValue = two if one < two else one 
    
    stack.append(smallerValue)
    sortStack(stack)
    stack.append(largerValue)
    
    return stack

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': [-5, 2, -2, 4, 3, 1],
        'output': [-5, -2, 1, 2, 3, 4],
        'active': False
    },
    'test_case_2': {
        'description': 'normal test',
        'input': [6, 5, 3, 7, 2, 5],
        'output': [2, 3, 5, 5, 6, 7],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = sortStack(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
