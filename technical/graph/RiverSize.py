def validPosition(matrix, i, j):
    if i in range(0, len(matrix)) and j in range(0, len(matrix[0])):
        return True
    return False

def riverSizes(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    
    queue = []
    result = []

    #Find all ones in the matrix
    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == 1:
                queue.append((i, j))

    while queue:
        
        current = queue.pop(0)
        
        currentCount = 1
        stack = [current]
        
        while stack:
            
            currentRiver = stack.pop()
            
            for jumpPosition in [[0,1], [1,0], [-1,0], [0, -1]]:
                
                x = currentRiver[0]+jumpPosition[0]
                y = currentRiver[1]+jumpPosition[1]
                
                if validPosition(matrix, x, y) and matrix[x][y] == 1 and (x, y) in queue:
                    currentCount += 1
                    stack.append((x, y))
                    queue.remove((x, y))

        result.append(currentCount)

    return sorted(result)

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

print(riverSizes(matrix))
