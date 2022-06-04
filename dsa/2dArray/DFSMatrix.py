def isvalid(grid, i, j):
    
    row = len(grid)
    col = len(grid[0])

    if i in range(0, row) and j in range(0, col):
        return True
    
    # @deprecate
    # if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
    #     return False

    return False


def change_color(grid, i, j, target_color):

    if not isvalid(grid, i, j):
        return -1

    # Initialize stack
    visited = []

    # Initial condition
    start_color = grid[i][j]
    visited.append((i, j))

    while visited:

        current_x, current_y = visited.pop()

        grid[current_x][current_y] = target_color
        
        #Checking adjcent and diagonal values
        #for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        
        #Checking adjcent values
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            jump_position_x = current_x + new_position[0]
            jump_position_y = current_y + new_position[1]

            if isvalid(grid, jump_position_x, jump_position_y) and grid[jump_position_x][jump_position_y] == start_color:
                visited.append((jump_position_x, jump_position_y))

    return grid


test_cases = {
    'test_case_1': {
        'description': 'Testing success',
        'input': {
            'grid': [['B', 'B', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W'], ['B', 'B', 'B']],
            'i': 2,
            'j': 2,
            'target_color': 'G'
        },
        'output': [['B', 'B', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G'], ['B', 'B', 'B']]
    },
    'test_case_2': {
        'description': 'Testing if start point is invalid',
        'input': {
            'grid': [['B', 'B', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W'], ['B', 'B', 'B']],
            'i': 4,
            'j': 4,
            'target_color': 'G'
        },
        'output': -1
    },
    'test_case_3': {
        'description': 'Testing if adjcent values are not start color',
        'input': {
            'grid': [['B', 'B', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'B', 'B']],
            'i': 2,
            'j': 2,
            'target_color': 'G'
        },
        'output': [['B', 'B', 'W'], ['W', 'W', 'B'], ['W', 'B', 'G'], ['B', 'B', 'B']]
    },
    'test_case_4': {
        'description': 'Testing if start color is same as target color',
        'input': {
            'grid': [['B', 'B', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'B', 'B']],
            'i': 2,
            'j': 2,
            'target_color': 'W'
        },
        'output': [['B', 'B', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'B', 'B']]
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    input = data['input']
    result = change_color(input['grid'], input['i'],
                            input['j'], input['target_color'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Output: ', end="")
        print(result)
