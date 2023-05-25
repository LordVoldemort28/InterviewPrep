#https: // www.hackerrank.com/challenges/poisonous-plants/problem
#!/bin/python3

#T -> O(n^2)
def poisonousPlantsBruteForce(p):
    maxDays = 0
    
    while True:
        
        stack = [p[0]]
        for idx in range(1, len(p)):
            if p[idx] > p[idx-1]:
                continue
            stack.append(p[idx])
        
        if stack == p:
            break
        maxDays += 1
        p = stack
            
    return maxDays

#T -> O(n)
def poisonousPlants(p):
    stack = [(p[0], 0)]
    maxDays = 0

    for idx in range(1, len(p)):
        
        if p[idx] > p[idx-1]:
            stack.append((p[idx], 1))
            maxDays = max(maxDays, 1)
        else:
            n = 0
            while stack and stack[-1][0] >= p[idx]:
                n = max(n, stack[-1][1])
                stack.pop()

            dayToDie = 0 if len(stack) == 0 else n+1
            maxDays = max(dayToDie, maxDays)
            stack.append((p[idx], dayToDie))
        
    return maxDays


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [6, 5, 8, 4, 7, 10, 9],
        'output': 2,
        'active': True
    },
    'test_case_0': {
        'description': 'cycle test',
        'input': [3, 6, 2, 7, 5],
        'output': 2,
        'active': True
    },
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = poisonousPlants(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
