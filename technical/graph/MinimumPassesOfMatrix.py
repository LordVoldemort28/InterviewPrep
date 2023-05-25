#Flood fill
def isValidIdx(i, j, matrix):
    return i in range(len(matrix)) and j in range(len(matrix[0]))

def getNegativeEdges(matrix):
    negativeEdges = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                negativeEdges.append((i, j))

    return negativeEdges

def minimumPassesOfMatrix(matrix):
    
    #Get all negative edges from matrix
    currentNegativeEdges = getNegativeEdges(matrix)
    
    #Number of rounds to convert all positive
    round = 0
    
    #Doesn't have anything to convert positive
    if not currentNegativeEdges:
        return round
    
    while currentNegativeEdges:
        
        #Keeping set to store the negative edges which can be converted
        #to positive
        #Why??? To not change value on fly when we are checking all negatives
        canChange = set()
        for edge in currentNegativeEdges:
            
            #Check all adjacent position 
            for adjPos in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                
                x = edge[0] + adjPos[0]
                y = edge[1] + adjPos[1]
                
                #If the adjacent value is valid and positive
                if isValidIdx(x, y, matrix) and matrix[x][y] > 0:
                    canChange.add(edge)
                    break
        
        #Convert negative integers which can be change to positive
        for edge in canChange:
            matrix[edge[0]][edge[1]] *= -1
        
        prevNegativeEdges = currentNegativeEdges
        currentNegativeEdges = getNegativeEdges(matrix)
        
        #Checking if there's any diff from previous negative edges
        #to new set of negative edges
        #If there's no changes then return not possible to convert to positive
        if prevNegativeEdges == currentNegativeEdges:
            return -1
        
        #Update round performed
        round += 1

    return round

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': [
            [0, -2, -1],
            [-5, 2, 0],
            [-6, -2, 0]
        ],
        'output': 2,
        'active': True
    },
    'test_case_2': {
        'description': 'not possible to convert all positive',
        'input': [
            [-1, 0, 3],
            [0, -5, -6]
        ],
        'output': -1,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = minimumPassesOfMatrix(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)