#Check if current position is cor
def isCorner(matrix, i, j):
    if i == 0 or j == 0 or i == len(matrix)-1 or j == len(matrix[0]) - 1:
        return True
    return False

def isValidPosition(matrix, i, j):
    if i in range(0, len(matrix)) and j in range(0, len(matrix[0])):
        return True
    return False

def removeIsland(matrix):
    
    
    rows = len(matrix)
    cols = len(matrix[0])
    queue = []
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not isCorner(matrix, i, j):
                queue.append((i, j))
    
    while queue:
        
        curr = queue.pop(0)
        stack = [curr]
        removeIslands = []
        
        while stack:
            
            currIsland = stack.pop()
            removeIslands.append(currIsland)
            
            if isCorner(matrix, currIsland[0], currIsland[1]):
                removeIslands = []
                break
            
            for adjPosition in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                
                x = currIsland[0] + adjPosition[0]
                y = currIsland[1] + adjPosition[1]
                
                if isValidPosition(matrix, x, y) and matrix[x][y] == 1:
                    
                    if (x, y) not in removeIslands:
                        stack.append((x, y))

        for island in removeIslands:
            x, y = island
            matrix[x][y] = 0
            if (x, y) in queue:
                queue.remove((x, y))
    
    return matrix

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

expectedMatrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

print(removeIsland(matrix) == expectedMatrix)


