class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #Lets assume that all numbers till n are primes
        dp = [True] * n
        
        #We know they are not
        dp[0] = dp[1] = False
        
        
        for number in range(2, n):
            
            #if its prime then eliminate multiples of this number
            #For example 3 is prime then eliminate 6, 9, 12.....
            if dp[number]:
                
                #Taking 2*number means leave current number and eliminate next multiple
                for multiple in range(2*number, n, number):
                    dp[multiple] = False
            
        return sum(dp)
    
test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': 10,
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
    result = Solution().countPrimes(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
