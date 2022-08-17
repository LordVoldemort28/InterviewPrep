class Solution:
    def getMaximumGold(self, grid):
        
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                
                up = grid[i-1][j] if i-1 in range(row) else 0
                left = grid[i][j-1] if j-1 in range(col) else 0
                
                grid[i][j] = max(left, up) + grid[i][j]
        print(grid)
        return grid[-1][-1]


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [
            [0, 6, 0],
            [5, 8, 7],
            [0, 9, 0]
        ],
        'output': 23,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [[1, 0, 7],
                  [2, 0, 6],
                  [3, 4, 5],
                  [0, 3, 0],
                  [9, 0, 20]],
        'output': 28,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    tool = Solution()
    result = tool.getMaximumGold(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
