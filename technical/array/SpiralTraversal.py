class Direction:

    def __init__(self, coor):
        self.coor = coor
        self.next = None
        self.previous = None


def get_path():

    right = Direction([0, 1])
    left = Direction([0, -1])
    up = Direction([-1, 0])
    down = Direction([1, 0])

    # Define forward steps
    right.next = down
    down.next = left
    left.next = up
    up.next = right

    # Define backward steps
    right.previous = left
    left.previous = right
    up.previous = down
    down.previous = up

    return right


def isValidPosition(array, x, y):
    return x in range(0, len(array)) and y in range(0, len(array[0]))


def spiralTraverse(array):
   # Write your code here.

    rows, cols = len(array), len(array[0])
    total_items = rows * cols

    visited = [[False for i in range(0, cols)] for j in range(0, rows)]

    current = [0, 0]
    visited[0][0] = True
    direction = get_path()

    output = [array[0][0]]

    while True:

        x = current[0] + direction.coor[0]
        y = current[1] + direction.coor[1]

        if len(output) == total_items:
            break

        if not isValidPosition(array, x, y):
            direction = direction.next
        elif visited[x][y] == True:
            direction = direction.next
        else:
            output.append(array[x][y])
            visited[x][y] = True
            current[0], current[1] = x, y

    return output


test_cases = {
    'test_case_1': {
        'description': 'Square test',
        'input': [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ],
        'output': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        'active': True
    },
    'test_case_2': {
        'description': 'Rectangle test',
        'input': [
            [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
            [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
        ],
        'output': [4, 2, 3, 6, 7, 8, 1, 9, 5, 10, 14, 11, 17, 13, 18, 20, 16, 15, 19, 12],
        'active': True
    }
}


for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = spiralTraverse(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()