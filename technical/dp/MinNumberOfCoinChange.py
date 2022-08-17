def minNumberOfCoinsForChange(n, denoms):                                                                                                                                           
    #Adding additional rows and cols to include base case
    rows = len(denoms)+1
    cols = n+1

    dp = [[float("inf")] * cols] * rows

    for i in range(rows):
        dp[i][0] = 0
    print(dp[0])
    for coinIdx in range(1, rows):
        for amount in range(1, cols):

            coinValue = denoms[coinIdx-1]

            #If amount is bigger than denom
            #Check if set min of value above or (best amount after negating coinValue plus one)
            if amount >= coinValue:
                dp[coinIdx][amount] = min(
                    dp[coinIdx-1][amount], (dp[coinIdx][amount-coinValue]+1))
            else:
                dp[coinIdx][amount] = dp[coinIdx-1][amount]
        print(dp[coinIdx])

    result = dp[rows-1][cols-1]

    return result if result != float("inf") else -1

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': {
            'n': 7,
            'denoms': [1, 5, 10]
        },
        'output': 3,
        'active': True
    },
    'test_case_2': {
        'description': 'big test',
        'input': {
            "denoms": [1, 5, 10, 25],
            "n": 25
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
    result = minNumberOfCoinsForChange(input['n'], input['denoms'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
