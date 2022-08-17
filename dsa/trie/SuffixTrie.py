class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for idx in range(len(string)):
            self.insert(string[idx:])
        return

    def insert(self, string):
        c_node = self.root
        
        for letter in string:
            if letter not in c_node.keys():
                c_node[letter] = {}
            c_node = c_node[letter]
        c_node["*"] = True

    def contains(self, string):
        
        c_node = self.root
        for letter in string:
            
            if letter not in c_node.keys():
                return False
            c_node = c_node[letter]
            
        return '*' in c_node.keys()


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'string': 'babc',
            'contains': 'abc'
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
    tool = SuffixTrie(input['string'])
    result = tool.contains(input['contains'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
