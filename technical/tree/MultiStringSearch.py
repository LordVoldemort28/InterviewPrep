class TrieDict:

    def __init__(self):
        self.root = {"*": "*"}

    def populateSuffixTrieFrom(self, string):
        for idx in range(len(string)):
            self.insert_word(string[idx:])
        return

    def insert_word(self, word):

        c_node = self.root

        for letter in word:
            if letter not in c_node:
                c_node[letter] = {}
            c_node = c_node[letter]

        c_node["*"] = "*"

    def has_prefix(self, word):

        c_node = self.root

        for letter in word:
            if letter not in c_node:
                return False
            c_node = c_node[letter]

        return True


def multiStringSearch(bigString, smallStrings):

    trie = TrieDict()

    for word in bigString.split(' '):
        trie.populateSuffixTrieFrom(word)

    return [trie.has_prefix(word) for word in smallStrings]


test_cases = {
    'test_case_1': {
        'description': 'multi words',
        'input': {
            'bigString': "this is a big string",
            'smallStrings': ["this", "yo", "is", "a", "bigger", "string", "kappa"]      
        },
        'output': [True, False, True, True, False, True, False],
        'active': True
    },
    'test_case_2': {
        'description': 'single test',
        'input': {
            'bigString': "abcdefghijklmnopqrstuvwxyz",
            'smallStrings': ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]
        },
        'output': [True, True, False, True, True, False],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = multiStringSearch(input['bigString'], input['smallStrings'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
