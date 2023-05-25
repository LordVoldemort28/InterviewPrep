class Solution(object):
    def strStrBruteForce(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        n = len(haystack)
        m = len(needle)

        for i in range(n):

            if haystack[i] == needle[0]:
                #Edge case where needle is only of length 1
                if m == 1:
                    return i

                p = 1
                for j in range(i+1, n):

                    if haystack[j] == needle[p]:
                        p += 1

                        if p == m:
                            return i
                    else:
                        break

        return -1

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        for i in range(n):

            if haystack[i] == needle[0]:
                #Edge case where needle is only of length 1
                if m == 1:
                    return i

                if haystack[i:(i+m)] == needle:
                    return i

        return -1


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'haystack': "sabjsdfkljasad",
            'needle': "sab"
        },
        'output': 0,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'haystack': "as",
            'needle': "s"
        },
        'output': 1,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': {
            'haystack': "mississippi",
            'needle': "issip"
        },
        'output': 4,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().strStr(input['haystack'], input['needle'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
