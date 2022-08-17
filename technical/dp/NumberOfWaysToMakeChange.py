def numberOfWaysToMakeChange(n, denoms):

    #If target sum of coins is 0 then there's only one way
    # to not use any denominations
    if n < 1:
        return 1

    nCoins = len(denoms)
    
    #base case of 0
    cols = n+1

    ways = [0] * cols

    ways[0] = 1
    print([amount for amount in range(cols)])
    for i in range(nCoins):
        for amount in range(cols):

            if amount >= denoms[i]:
                ways[amount] += ways[amount - denoms[i]]
        print(ways)
    return ways[n]


test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': {
            'n': 6,
            'denoms': [1, 5]
        },
        'output': 2,
        'active': True
    },
    'test_case_2': {
        'description': 'big test',
        'input': {
            "denoms": [1, 5, 10, 25],
            "n": 25
        },
        'output': 13,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = numberOfWaysToMakeChange(input['n'], input['denoms'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
