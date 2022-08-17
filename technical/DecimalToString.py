def decimalToString(numerator, denominator):
    
    n, remainder = divmod(abs(numerator), abs(denominator))
    
    sign = '-' if numerator*denominator < 0 else ''
    result = [sign+str(n)]
    if remainder == 0:
        return ''.join(result)

    result.append('.')
    dic = {}
    while remainder != 0:

        if remainder in dic:
            result.insert(dic[remainder], '(')
            result.append(')')
            break
        
        dic[remainder] = len(result)
        n, remainder = divmod(remainder*10, (denominator))
        result.append(str(n))
        
    return ''.join(result)

test_cases = {
    'test_case_1': {
        'description': 'non-repeating decimal',
        'input': (1, 2),
        'output': "0.5",
        'active': True
    },
    'test_case_2': {
        'description': 'integer',
        'input': (2, 1),
        'output': "2",
        'active': True
    },
    'test_case_3': {
        'description': 'repeating decimal',
        'input': (4, 333),
        'output': "0.(012)",
        'active': True
    },
    'test_case_4': {
        'description': 'negative non-repeating decimal',
        'input': (-2, 1),
        'output': "-2",
        'active': True
    },
    'test_case_5': {
        'description': 'negative repeating decimal',
        'input': (-100, 3),
        'output': "-33.(3)",
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = decimalToString(input[0], input[1])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
