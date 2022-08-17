def isValid(board, i, j):
    return i in range(len(board)) and j in range(len(board[0]))

def boggleBoard(board, words):
    
    result = []
    
    for word in words:
        if isWordOnBoard(board, word):
            result.append(word)
            
    return result

def isWordOnBoard(board, word):
    
    startPositions = []
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                startPositions.append((i, j))
    
    #There's no positions to start in board
    if len(startPositions) < 1:
        return False
    
    #If word is a single character
    if len(word) < 2:
        return True
    
    for position in startPositions:
        
        #Check if next word exist adjacent to start position
        if lookNextLetter(board, [position], 1, word):
            return True
        
    return False


def lookNextLetter(board, positions, letterIdx, word):
    
    #If all chars are looked
    if len(positions) == len(word):
        return True
    
    currentPosition = positions[-1]
    
    #Check all adjacent place
    for (jumpPositionX, jumpPositionY) in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        
        x = currentPosition[0] + jumpPositionX
        y = currentPosition[1] + jumpPositionY
        
        #If position is valid, position is visited before and next letter exists
        if isValid(board, x, y) and ((x, y) not in positions) and word[letterIdx] == board[x][y]:

            if lookNextLetter(board, (positions+[(x, y)]), (letterIdx+1), word):
                return True
            
            #Trace back and look for another path
            else:
                continue

    return False

test_cases = {
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
            'words': ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]
        },
        'output': ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"],
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
            'words': ["san", "sana", "at", "vomit", "yours", "help", "end", "been", "bed", "danger", "calm", "ok", "chaos", "complete", "rear", "going", "storm", "face", "epual", "dangerous"]
        },
        'output': ['san', 'at', 'yours', 'help', 'danger'],
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["f", "t", "r", "o", "p", "i", "k", "b", "o"],
                ["r", "w", "l", "p", "e", "u", "e", "a", "b"],
                ["j", "o", "t", "s", "e", "l", "f", "l", "p"],
                ["s", "z", "u", "t", "h", "u", "o", "p", "i"],
                ["k", "a", "e", "g", "n", "d", "r", "g", "a"],
                ["h", "n", "l", "s", "a", "t", "e", "t", "x"]
            ],
            'words': ["obligate", "frozen", "rotten", "teleport", "city", "zutgatz", "kappa", "before", "rope", "annoying"]
        },
        'output': ["before", "frozen", "kappa", "obligate", "rope", "rotten", "teleport"],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = boggleBoard(input['board'], input['words'])
    if sorted(result) == sorted(data['output']):
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
