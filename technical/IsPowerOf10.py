import math

def isPowerOf10Log(number):
    if number < 1:
        return False
    result = math.log10(number)
    return result == int(result)

def isPowerOf10(number):
    
    if number%10 != 0 or number < 1:
        return False
    
    while number > 1:
        number /= 10
    
    return number == 1


test_cases = {
    'test_case_1': {
        'description': 'power of 10 test',
        'input': 100000,
        'output': True,
        'active': True
    },
    'test_case_2': {
        'description': 'not power of 10 test',
        'input': 101,
        'output': False,
        'active': True
    },
    'test_case_3': {
        'description': 'not power of 10 test',
        'input': 150,
        'output': False,
        'active': True
    },
    'test_case_4': {
        'description': 'zero test',
        'input': 1,
        'output': False,
        'active': True
    },
    'test_case_5': {
        'description': 'negative test',
        'input': -10,
        'output': False,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = isPowerOf10(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
