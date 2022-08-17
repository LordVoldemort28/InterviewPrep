def arrayOfProducts(array):

    products = [1 for _ in range(len(array))]
    
    #Taking base case as 1 and 
    leftRunningProduct = 1
    for i in range(len(array)):
        
        #Memoizing previous multiplications
        products[i] = leftRunningProduct
        
        #Base case into current element
        leftRunningProduct *= array[i]

    #Memoizing multiplications from right
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [5, 1, 4, 2],
        'output': [8, 40, 10, 20],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = arrayOfProducts(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
