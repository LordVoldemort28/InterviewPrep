from collections import Counter

class Solution:
    def minWindowBruteForce(self, s, t):
        m = len(s)
        n = len(t)
        
        if n > m:
            return ""
        if n == 1 and m == 1:
            return s if s == t else ""
        
        #Size of second string will be lowest window size
        currentWindowSize = n
        
        minWindowSize = float("inf")
        minSubstring = ""

        for size in range(currentWindowSize, (m+1)):
            
            left = 0
            right = left + size
            
            while right < (m+1):
                
                substring = s[left:right]
                
                if self.doesExist(substring, t) and len(substring) < minWindowSize:
                    minWindowSize = len(substring)
                    minSubstring = substring
                    
                left += 1
                right += 1
                
        return minSubstring
    
    def doesExist(self, s, t):
        
        for letter in t:
            if letter not in s:
                return False
            
        return True
    
    def minWindow(self, s, t):
        
        sCount, tCount = Counter(), Counter(t)
        left, right = 0, 0
        m= len(s)
        
        result = ""
        minLength = float("inf")
        
        while right <= m-1:
            
            #Find valid window
            sCount[s[right]] += 1
            right += 1
            
            #Check if t exist in substring
            # & -> will help in finding junction between both counters
            if (sCount & tCount) != tCount:
                continue
            
            #Minimize this window
            while left < right:
                
                #Remove one char from left
                sCount[s[left]] -= 1
                left += 1
                
                if (sCount & tCount) == tCount:
                    continue
                
                substring = s[(left-1):right]
                
                if len(substring) <= minLength:
                    result = substring
                    minLength = len(substring)
                
                # results.append(s[(left-1):right])
                break
        return result
        # return min(results, key=len) if results else ""

test_cases = {
    'test_case_5': {
        'description': 'cycle test',
        'input': ['abc', 'cba'],
        'output': 'abc',
        'active': True
    },
    'test_case_4': {
        'description': 'cycle test',
        'input': ['abc', 'ac'],
        'output': 'abc',
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': ['a', 'a'],
        'output': 'a',
        'active': True
    },
    'test_case_1': {
        'description': 'cycle test',
        'input': ['ADOBECODEBANC', 'ABC'],
        'output': 'BANC',
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': ['a', 'aa'],
        'output': '',
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().minWindow(input[0], input[1])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
