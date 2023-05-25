class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.wordOnBoard(board, word, 1, (i, j)):
                    return True
                
        return False
        
    def wordOnBoard(self, board, word, letterIdx, move):
        
        if len(word) == letterIdx:
            return True
        
        (currX, currY) = move
        
        temp = board[currX][currY]
        board[currX][currY] = '~'
        
        for (jumpPositionX, jumpPositionY) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            x = currX + jumpPositionX
            y = currY + jumpPositionY
            
            if x in range(len(board)) and y in range(len(board[0])) and word[letterIdx] == board[x][y]:
                if self.wordOnBoard(board, word, (letterIdx+1), (x, y)):
                    return True
                else: continue

        board[currX][currY] = temp
        return False

test_cases = {
    'test_case_5': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["C", "A", "A"],
                ["A", "A", "A"],
                ["B", "C", "D"]
            ],
            'words': "AAB"
        },
        'output': True,
        'active': True
    },
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["t", "h", "i", "s", "i", "s", "a"],
                ["s", "i", "m", "p", "l", "e", "x"],
                ["b", "x", "x", "x", "x", "e", "b"],
                ["x", "o", "g", "g", "l", "x", "o"],
                ["x", "x", "x", "D", "T", "r", "a"],
                ["R", "E", "P", "E", "A", "d", "x"],
                ["x", "x", "x", "x", "x", "x", "x"],
                ["N", "O", "T", "R", "E", "-", "P"],
                ["x", "x", "D", "E", "T", "A", "E"]
            ],
            'words': 'this'
        },
        'output': True,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["y", "g", "f", "y", "e", "i"],
                ["c", "o", "r", "p", "o", "u"],
                ["j", "u", "z", "s", "e", "l"],
                ["s", "y", "u", "r", "h", "p"],
                ["e", "a", "e", "g", "n", "d"],
                ["h", "e", "l", "s", "a", "t"]
            ],
            'words': "san"
        },
        'output': True,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["A", "B", "C", "E"], 
                ["S", "F", "C", "S"], 
                ["A", "D", "E", "E"]
            ],
            'words': "SEE"
        },
        'output': True,
        'active': True
    },
    'test_case_4': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["A", "A", "A", "A", "A", "A"], 
                ["A", "A", "A", "A", "A", "A"], 
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"], 
                ["A", "A", "A", "A", "A", "A"], 
                ["A", "A", "A", "A", "A", "A"]
            ],
            'words': "AAAAAAAAAAAABAA"
        },
        'output': False,
        'active': True
    },
    'test_case_4': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"]
            ],
            'words': "eat"
        },
        'output': True,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().exist(input['board'], input['words'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
