"""
You are given n numbers as well as n probabilities that sum up to 1. 
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers[1, 2, 3, 4] and probabilities[0.1, 0.5, 0.2, 0.2], 
your function should return 1 10 % of the time, 2 50 % of the time, and 3 and 4 20 % of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
from random import shuffle, choice

def generate_number(numbers, probabilites):
    bucket = []
    
    for idx, number in enumerate(numbers):
        frequency = int(probabilites[idx]*10)
        for _ in range(0, frequency):
            bucket.append(number)
    
    # shuffle(bucket)
    
    return choice(bucket)
    
test_cases = {
    'test_case_1': {
        'description': 'Testing success case',
        'input': {
            'numbers': [1, 2, 3, 4],
            'probabilites': [0.1, 0.5, 0.2, 0.2]
        },
        'output': 2
    }
}

for test_case, data in test_cases.items():
    
    print('Running -> {} -> {}'.format(test_case, data['description']))

    input = data['input']
    print(generate_number(input['numbers'], input['probabilites']))
