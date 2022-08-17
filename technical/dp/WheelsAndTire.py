"""
Recursive way to solve
Find all possible path and save the path if sum reaches to zero

to get unique path sort before saving
"""
def path(n):
    
    all_path = []
    
    def findWay(n, way=[]):
        
        if n == 0:
            way.sort()
            if way not in all_path:
                all_path.append(way)
        elif n > 1:
            findWay(n-2, way + [2])
            findWay(n-4, way + [4])
        return way
    
    findWay(n)
    return len(all_path)

#Solution - 2 Dynamic Approach
def wheelsAndTires(wheels):
    
    def getUniqueSets(wheel, tires=[2, 4]):
        
        nWheels = wheel+1
        
        #Make matrix to record number of ways for each possible from 0 to total wheel sum
        ways = [0] * nWheels
        
        #Init base case. if theres wheel is 0 then there's one way
        ways[0] = 1
        
        #Calculating possible ways by deducting sums
        for tire in tires:
            for neededWheel in range(nWheels):
                
                #If neededWheelSum is greater then tire size available 
                #Then trace back possible
                if neededWheel >= tire:
                    ways[neededWheel] += ways[neededWheel - tire]
        return ways[wheel]
    
    waysForAllWheels = getUniqueSets(max(wheels))
    
    result = [0] * len(wheels)
    
    for idx in range(len(result)):
        result[idx] = waysForAllWheels[wheels[idx]]
        
    return result

test_cases = {
    'test_case_1': {
        'description': 'big test',
        'input': [10, 6, 2, 3, 4, 11, 8],
        'output': [3, 2, 1, 0, 2, 0, 3],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = wheelsAndTires(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
