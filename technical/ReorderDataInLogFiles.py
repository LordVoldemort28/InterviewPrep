class Solution(object):
    def reorderLogFiles(self, rawLogs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        logs = Logs()

        for log in rawLogs:
            logs.insertLog(log)

        return logs.getWordLogs() + logs.getNumberLogs()

class WordLogs:
    
    def __init__(self, id, word):
        self.id = id
        self.word = word
        
    def __lt__(self, wordLog):
        if self.word == wordLog.word:
            return self.id < wordLog.id
        return self.word < wordLog.word
    
    def __str__(self):
        return "{} {}".format(self.id, " ".join(self.word))
    
class Logs:
    
    def __init__(self):
        self.numberLogs = []
        self.wordLogs = []
        
    def insertLog(self, log):
        
        log = log.split(' ')
        id, message = log[0], log[1:]
        
        if message[0].isnumeric():
            self.numberLogs.append(" ".join(log))
        else:
            self.wordLogs.append(WordLogs(id, message))
            
        return
    
    def getNumberLogs(self):
        return self.numberLogs
    
    def getWordLogs(self):
        return [str(wordLog) for wordLog in sorted(self.wordLogs)]

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
        'output': ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
        'output': ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
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
    result = tool.reorderLogFiles(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
