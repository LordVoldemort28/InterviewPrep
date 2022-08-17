from collections import Counter

class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for substring in self.substrings(s):
            print(substring)
            print(self.getUniqueLetterCount(substring))
            
        return sum
    
    def getUniqueLetterCount(self,s):
        
        counter = Counter(s)
        sum = 0
        for _, count in counter.items():
            if count == 1:
                sum += 1
                
        return sum

    def substrings(self, word):
        return set([word[i: j] for i in range(len(word))
                    for j in range(i + 1, len(word) + 1)])

tool = Solution()
print(tool.uniqueLetterString('aba'))

