from collections import defaultdict
from heapq import heappop, heappush

class HeapNode:
    
    def __init__(self, word):
        self.word = word
        self.count = 1
        
    def update(self):
        self.count += 1
    
    def __lt__(self, node):
        if self.count == node.count:
            return self.word > node.word
        return self.count < node.count
    
    def __eq__(self, word):
        return self.word == word
    
    def __str__(self):
        return self.word
    
class Solution(object):
    def topKFrequentHeap(self, words, k):

        heapWords = []
        for word in words:
            if word not in heapWords:
                heapWords.append(HeapNode(word))
            else:
                heapWords[heapWords.index(word)].update()

        heapWords.sort(reverse=True)

        return [str(heapWords[idx]) for idx in range(0, k)]

    def topKFrequent(self, words, k):
        
        count = defaultdict(int)
        freq = defaultdict(list)
        
        for word in words:
            count[word] += 1

        for word, frequency in count.items():
            freq[frequency].append(word)
        
        counter = 0
        res = []
        for i in reversed(range(len(words)+1)):
            
            if i not in freq:
                continue
            
            for word in freq[i]:
                
                res.append(word)
                counter += 1
                
                if counter == k: return res
        
        return res

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [["i", "love", "leetcode", "i", "love", "coding"], 2],
        'output': ["i", "love"],
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4],
        'output': ["the", "is", "sunny", "day"],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().topKFrequent(input[0], input[1])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
