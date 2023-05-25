class Solution(object):
    def intToRoman(self, num):

        ROMAN = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        result = []

        for digit, value in ROMAN:

            if num == 0:
                break

            count, num = divmod(num, digit)

            result.append(value*count)

        return "".join(result)
        
test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': 3,
        'output': "III",
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': 58,
        'output': "LVIII",
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': 1994,
        'output': "MCMXCIV",
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().intToRoman(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
