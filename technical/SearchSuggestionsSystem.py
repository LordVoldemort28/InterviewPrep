class TrieDict:

    def __init__(self):
        self.root = {"*": "*"}

    def insert_word(self, word):

        c_node = self.root

        for letter in word:
            if letter not in c_node:
                c_node[letter] = {}
            c_node = c_node[letter]

        c_node["*"] = "*"
    
    def dfs(self, node, words, result):

        for letter, children in node.items():

            if letter == "*":
                result.append(''.join(words))
            else:
                self.dfs(children, (words+letter), result)

        return result
    
    def trieDFS(self, searchWord):
        
        cNode = self.root
        word = ""
        suggestions = []
        
        for letter in searchWord:
            
            word += letter
            if letter not in cNode:
                return []
            cNode = cNode[letter]
            topSearch = sorted(self.dfs(cNode, word, []))[:3]
            suggestions.append(topSearch)
            
        return suggestions
        
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = TrieDict()
        
        for product in products:
            trie.insert_word(product)
            
        trie.trieDFS(searchWord)

        return trie.trieDFS(searchWord)

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'products': ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            'searchWord': "mouse"
        },
        'output': [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']],
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
    result = tool.suggestedProducts(input['products'], input['searchWord'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()

"""
class TrieDict:

    def __init__(self):
        self.root = {"*": "*"}

    def insert_word(self, word):

        c_node = self.root

        for letter in word:
            if letter not in c_node:
                c_node[letter] = {}
            c_node = c_node[letter]

        c_node["*"] = "*"
    
    def trieDFS(self, word):
        
        cNode = self.root
        
        for letter in word:
            if letter not in cNode:
                return []
            cNode = cNode[letter]
        
        result = []
        
        def dfs(node, words):
            
            for letter, children in node.items():
                
                if letter == "*":
                    result.append(''.join(words))
                else:
                    dfs(children, (words+letter))
                
            return
        
        dfs(cNode, word)
        
        return sorted(result)[:3]
        
class Solution(object):
    def suggestedProducts(self, products, searchWord):

        trie = TrieDict()
        result = []
        
        for product in products:
            trie.insert_word(product)
            
        for idx in range(len(searchWord)):
            result.append(trie.trieDFS(searchWord[:(idx+1)]))

        return result
"""
