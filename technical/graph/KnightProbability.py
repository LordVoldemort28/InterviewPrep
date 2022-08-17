#https://leetcode.com/problems/knight-probability-in-chessboard/
def isValidMove(n, i, j):
    return i in range(n) and j in range(n)

def getMoves():
    return [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]

def knightProbabilityBFS(n, k, row, col):
    
    #Probability of each position
    K = 1/8
    
    queue = []
    
    #Starting with given position and probability of current position to be 1
    #because current position is guaranteed 
    queue = [(row, col, 0, 1)]
    finalProbability = 0
    
    while queue:
        
        currX, currY, totalMove, currentProbability = queue.pop(0)
        
        if totalMove == k:
            finalProbability += currentProbability
        else:
            for (jumpPositionX, jumpPositionY) in getMoves():
                
                x, y = (currX + jumpPositionX), (currY+jumpPositionY)
                
                if isValidMove(n, x, y):
                    queue.append((x, y, (totalMove+1), (currentProbability*K)))

    return finalProbability

""""
Dynamic approach
T -> O(n^2 * k)
S -> O(n^2)
"""
def knightProbability(n, k, row, col):
    
    K = 1/8
    possibleMoves = getMoves()
    
    memo = [[0 for _ in range(n)] for _ in range(n)]
    memo[row][col] = 1
    
    for _ in range(k):
        
        newMemo = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                
                for (jumpPositionX, jumpPositionY) in possibleMoves:
                    x, y = (i + jumpPositionX), (j+jumpPositionY)

                    if isValidMove(n, x, y):
                        newMemo[x][y] += memo[i][j] * K
        memo = newMemo
    
    finalProbability = 0
    for i in range(n):
        for j in range(n):
            finalProbability += memo[i][j]
        
    return finalProbability

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [3, 2, 0, 0],
        'output': 0.06250,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = knightProbability(input[0], input[1], input[2], input[3])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
