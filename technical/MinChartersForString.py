from collections import defaultdict, Counter

def minimumCharactersForWords(words):

    overallCounter = defaultdict(int)

    for word in words:

        localCounter = Counter(word)

        for letter, count in localCounter.items():

            if letter not in overallCounter.keys():
                overallCounter[letter] = count
            elif count > overallCounter[letter]:
                overallCounter[letter] = count
                
    result = []
    
    for key, value in overallCounter.items():
        for _ in range(value):
            result.append(key)

    return result


input = ["this", "that", "did", "deed", "them!", "a"]
output = ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']

print(minimumCharactersForWords(input) == output)

