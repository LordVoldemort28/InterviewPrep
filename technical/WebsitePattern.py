from collections import defaultdict, Counter
from itertools import combinations


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        MAX_WEBSITES = 3
        userLogs = defaultdict(list)
        
        # Sort first based on user, then time (grouping by user)
        for _, user, web in sorted(zip(timestamp, username, website)):
            userLogs[user].append(web)
        
        patterns = Counter()
        
        # Get unique 3-sequence (note that website order will automatically be maintained)
        # Note that we take the set of each 3-sequence for each user as they may have repeats
        # For each 3-sequence, count number of users
        for user, sites in userLogs.items():
            websiteCombinations = set(combinations(sites, MAX_WEBSITES))
            
            #Update counts
            patterns.update(Counter(websiteCombinations))

        maxCount = 0
        maxPattern = None
        
        for pattern, count in patterns.items():
            if count > maxCount:
                maxCount = count
                maxPattern = pattern
            #If count are same then return lexo max
            elif count == maxCount and maxPattern > pattern:
                maxPattern = pattern
                
        return maxPattern

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'username': ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
            'website': ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"],
            'timestamp': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
        'output': ('home', 'about', 'career'),
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'username': ["uod", "uod", "uod", "kfuagsh", "uod"],
            'website': ["bfx", "taohbuuleq", "vsryf", "irmbcoebt", "bfx"],
            'timestamp': [520778108, 799976888, 522803143, 968158505, 908405336]
        },
        'output': ('bfx', 'taohbuuleq', 'bfx'),
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
    result = tool.mostVisitedPattern(input['username'], input['timestamp'], input['website'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
