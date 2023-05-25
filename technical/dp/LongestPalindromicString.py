def isPalindrome(string):
    high = len(string)-1
    low = 0
    
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
        
    return True

"""
Brute force can be to produce all possible substring 
by sliding window approach. Then check all substring
for palindrome and store the max length possible.
Time complexity -> O(n^2)
Space complexity -> O(1)
"""
def longestPalindromicSubstringForce(string):
    lengthLongestPalindrome = float("-inf")
    longestSubstringPalindrome = None
    nChars = len(string)
    
    #Taking window from 1 char to length of string
    for window in range(1, nChars+1):
        for start in range(0, nChars):
            if (start+window) > nChars:
                continue
            #Getting substring from start idx to number of chars in window
            substring = string[start:(start+window)]
            if isPalindrome(substring) and \
                len(substring) > lengthLongestPalindrome:
                lengthLongestPalindrome = len(substring)
                longestSubstringPalindrome = substring
                
    return longestSubstringPalindrome
"""
For odd substring we can go with approach of 
pivoting at each character and going left and right
from that character till it forms a palindrome
Time complexity -> O(n^2)
"""
"""
Manachers's Algorithm
Time complexity -> O(n)
"""
test_cases = {
    'test_case_1': {
        'description': 'even test',
        'input': 'abaxyzzyxf',
        'output': 'xyzzyx',
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = longestPalindromicSubstring(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
