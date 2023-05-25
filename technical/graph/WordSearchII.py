from collections import defaultdict

class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

class Solution(object):
    
    def findWords(self, board, words):
        res = []
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, "", res)
        
        return res
    
    def dfs(self, board, node, i, j, path, res):
        
        if node.isWord:
            res.append(path)
            node.isWord = False
            
        if i not in range(len(board)) or j not in range(len(board[0])):
            return
        
        temp = board[i][j]
        node = node.children.get(temp)
        
        if not node:
            return
        
        board[i][j] = '~'
        
        for (jumpPositionX, jumpPositionY) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            
                x = i + jumpPositionX
                y = j + jumpPositionY
                
                self.dfs(board, node, x, y, (path+temp), res)
        
        board[i][j] = temp
        
test_cases = {
    'test_case_5': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["o", "a", "a", "n"], 
                ["e", "t", "a", "e"], 
                ["i", "h", "k", "r"], 
                ["i", "f", "l", "v"]
            ],
            'words': ["oath", "pea", "eat", "rain"]
        },
        'output': ["eat", "oath"],
        'active': True
    },
    'test_case_4': {
        'description': 'cycle test',
        'input': {
            'board': [
                ["a"]
            ],
            'words': ["a"]
        },
        'output': ["a"],
        'active': True
    },
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().findWords(input['board'], input['words'])
    if sorted(result) == sorted(data['output']):
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
