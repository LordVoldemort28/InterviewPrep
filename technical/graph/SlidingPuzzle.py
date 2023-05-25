from copy import deepcopy

#Sliding puzzle
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        expectedBoard = [[1,2,3], [4,5,0]]
        
        n, m = len(board), len(board[0])
        visited = set()
        queue = []
        totalMoves = 0
        
        #Get initial position of 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    queue.append((i, j, board.copy()))

        #Start sliding
        while queue:
            
            for _ in range(len(queue)):
                
                x, y, currentStateBoard = queue.pop(0)
                visited.add(str(currentStateBoard))
                
                if currentStateBoard == expectedBoard:
                    return totalMoves
                
                #Find neighbors
                for (jpx, jpy) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    
                    npX = jpx+x
                    npY = jpy+y
                    
                    if npX not in range(n) or npY not in range(m):
                        continue
                    
                    #Swap
                    board[x][y], board[npX][npY] = board[npX][npY],  board[x][y]
                    
                    if str(board) not in visited:
                        queue.append((npX, npY, deepcopy(board)))
                    
                    #Put state back for another move on current state
                    board[npX][npY], board[x][y] = board[x][y], board[npX][npY]
            
            totalMoves += 1
        
        return -1


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [[1, 2, 3], [4, 0, 5]],
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
    result = Solution().slidingPuzzle(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
