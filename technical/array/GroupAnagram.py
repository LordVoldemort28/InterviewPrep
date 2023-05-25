from collections import defaultdict

"""
Brute for anagram

Other approach
1. For every word make counter dict and do run length encoding
and assign it as key
"""
def groupAnagrams(words):
    anagrams = defaultdict(list)

    for word in words:
        anagrams[''.join(sorted(word))].append(word)
    
    return [value for value in anagrams.values()]

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"],
        'output': [['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo']],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = groupAnagrams(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
