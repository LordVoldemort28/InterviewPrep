"""
Brute Force approach where I'm traveling from each city
and checking if fuel left is positive or zero
and I'm returning to starting city

Time complexity: O(n^2)
Space complexity: O(1)
"""
def validStartingCity(distances, fuel, mpg):
    
    def calculateFuelLeft(idx):
        return (fuel[idx]*mpg)-distances[idx]
    
    nCities = len(distances)

    for idx in range(0, nCities):
        
        fuelLeft = calculateFuelLeft(idx)
        
        if fuelLeft <= 0:
            continue

        currentIdx = (idx+1) % nCities
        startIdx = idx
        totalSum = fuelLeft

        while totalSum >= 0:

            if currentIdx == startIdx:
                return currentIdx

            #for circular traversal
            totalSum += calculateFuelLeft(currentIdx)
            currentIdx = (currentIdx+1) % nCities

    return -1


test_cases = {
    'test_case_1': {
        'description': 'big test',
        'input': {
            'distances': [5, 25, 15, 10, 15],
            'fuel': [1, 2, 1, 0, 3],
            'mpg': 10
        },
        'output': 4,
        'active': True
    },
    'test_case_2': {
        'description': 'no test',
        'input': {
            'distances': [1, 3, 10, 6, 7, 7, 2, 4],
            'fuel': [1, 1, 1, 1, 1, 1, 1, 1],
            'mpg': 5
        },
        'output': 6,
        'active': True
    },
    'test_case_3': {
        'description': 'wrong test',
        'input': {
            'distances': [30, 40, 10, 10, 17, 13, 50, 30, 10, 40],
            'fuel': [1, 2, 0, 1, 1, 0, 3, 1, 0, 1],
            'mpg': 25
        },
        'output': 1,
        'active': True
    },
    'test_case_4': {
        'description': 'infinite test',
        'input': {
            'distances': [30, 40, 10, 10, 17, 13, 50, 30, 10, 40],
            'fuel': [10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'mpg': 25
        },
        'output': 0,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = validStartingCity(input['distances'], input['fuel'], input['mpg'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
