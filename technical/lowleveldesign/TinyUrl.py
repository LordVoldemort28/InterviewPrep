import hashlib
from secrets import choice


class Codec:
    
    def __init__(self):
        self.charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.urls = {}
        
    def getKey(self):
        return ''.join(choice(self.charset) for i in range(6))

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = self.getKey()
        while key in self.urls:
            key = self.getKey()
        
        self.urls[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[shortUrl.rindex('/')+1:]
        return self.urls[key] if key in self.urls else ''


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': "https://leetcode.com/problems/design-tinyurl",
        'output': "https://leetcode.com/problems/design-tinyurl",
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Codec(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
