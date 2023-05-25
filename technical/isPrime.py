def isPrime(n):
    
    if n < 2:
        return False
    
    for i in range(2, n):
        
        if n%i == 0:
            return False
        
    return True

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': 11,
        'output': True,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = isPrime(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
