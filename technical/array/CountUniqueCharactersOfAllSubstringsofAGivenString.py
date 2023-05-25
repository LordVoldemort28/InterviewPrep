from collections import defaultdict

"""
Taking an approach where we can put parentheses in all chars to for substring 
where that character will be unique

For example: "LEETCODE"

If I take the example of character E = [1, 2, 7] indexes occurrences

In case of E at index 1 at most character I can fit in left is going to be (index I'm at + 1) 
and on right its going to be (next occurrence - current position)

total substrings I can form is left * right
"""
class Solution:
    def uniqueLetterString(self, s):
        
        positions = defaultdict(list)
        n = len(s)
        sum = 0
        
        #First get the positions of each character
        for idx, char in enumerate(s):
            positions[char].append(idx)

        for indexes in positions.values():
            
            for i in range(len(indexes)):
                
                #Handling edge case where if theres no previous element then left is going to be currentPosition + 1
                left = indexes[i]+1 if i == 0 else indexes[i] - indexes[i-1] 
                
                #Handling edge case where if there's no next element then take all chars in string - current position
                right = n-indexes[i] if i == len(indexes)-1 else indexes[i+1] - indexes[i]
                
                sum += left*right
                
        return sum


test_cases = {
    # 'test_case_1': {
    #     'description': 'cycle test',
    #     'input': "ABA",
    #     'output': 8,
    #     'active': True
    # },
    'test_case_2': {
        'description': 'cycle test',
        'input': "LEETCODE",
        'output': 92,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': "ABC",
        'output': 10,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().uniqueLetterString(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
