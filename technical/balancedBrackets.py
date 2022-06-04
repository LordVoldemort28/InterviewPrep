def balancedBracket(string):

    stack = []

    close_bracket = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    allowed_brackets = [
        '[', ']',
        '(', ')',
        '{', '}'
    ]

    for item in string:

      if item not in allowed_brackets:
        continue

      if item not in close_bracket:
        stack.append(item)

      else:

        if len(stack) < 1:
          return False

        last = stack.pop()

        if last is not close_bracket[item]:
          return False

    if len(stack) > 0:
      return False

    return True


test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': '[[[[[()]]]]]',
        'output': True,
        'active': True
    },
    'test_case_2': {
        'description': 'croupt test',
        'input': '[[[[[(]]]]]',
        'output': False,
        'active': True
    },
    'test_case_3': {
        'description': 'letter test',
        'input': '(a)',
        'output': True,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
      print('Skipped!')
      continue

    input = data['input']
    result = balancedBracket(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
