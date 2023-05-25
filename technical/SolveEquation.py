class Solution(object):
    def solveEquation(self, equation):
        #Going in series and adding x values in coefficient and numerical in constants
        
        s = ''
        coeff, const = 0, 0
        right = False
        
        for num in equation:
            
            #Signed 
            if num in '+-':
                #Add value to total const and start new expression
                if s:
                    const += int(s or 0) * (right or -1)
                s = num
            elif num  == 'x':
                coeff -= int(s+'1' if s in '+-' else s) * (right or -1)
                s = ''
            elif num == '=':
                if s:
                    const -= int(s or 0)
                    s = ''
                right = True
            #Numerical value
            else:
                s += num

        if s:
            const += int(s or 0) * (right or -1)
        
        if coeff:
            return "x={}".format(const//coeff)
        else:
            if const:
                return 'No Solution'
            return 'Infinite Solution'

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': "x+5-3+x=6+x-2",
        'output': "x=2",
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().solveEquation(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
