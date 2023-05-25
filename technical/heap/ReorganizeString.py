from collections import Counter
from heapq import heappop, heappush

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = Counter(s)
        heap = []
        for ch, count in count.items():
            heappush(heap, (-count, ch))
        
        result = ""
        while len(heap) > 1:
            
            freq1, ch1 = heappop(heap)
            freq2, ch2 = heappop(heap)

            result += ch1
            result += ch2
            
            if abs(freq1) > 1:
                heappush(heap, (freq1+1, ch1))
            
            if abs(freq2) > 1:
                heappush(heap, (freq2+1, ch2))
                
        if not heap:
            return result

        freq, ch = heappop(heap)
        
        return "" if abs(freq) > 1 else (result+ch)
    
    def reorganizeString(self, s: str) -> str:

        counts = Counter(s)
        n = len(s)
        counts = sorted(counts.items(), key=lambda x: -x[1])

        #Because there should be a char with freq of half of string length
        if counts[0][1] >= n/2 + 1:
            return ""
        
        i = 0
        result = [""] * n
        for ch, freq in counts:
            for _ in range(freq):
                
                if i >= n:
                    i = 1
                    
                result[i] = ch
                i += 2

        return "".join(result)

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': "aab",
        'output': "aba",
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().reorganizeString(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
