def shortenPath(path):
    path = path.split('/')
    stack = [] if path[0] != '' else ['']

    for input in path:
        if input == '' or input == '.':
            continue
        if input == '..' and stack:
            if len(stack) == 1 and stack[0] == '':
                continue
            if stack[-1] == '..':
                stack.append(input)
            else:
                stack.pop()
            continue
        stack.append(input)
    
    if len(stack) == 1 and stack[0] == '':
        return '/'

    return '/'.join(stack)

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': "/foo/../test/../test/../foo//bar/./baz",
        'output': "/foo/bar/baz",
        'active': True
    },
    'test_case_2': {
        'description': 'normal test',
        'input': "foo/bar/baz",
        'output': "foo/bar/baz",
        'active': True
    },
    'test_case_3': {
        'description': 'normal test',
        'input': "../../foo/bar/baz",
        'output': "../../foo/bar/baz",
        'active': True
    },
    'test_case_4': {
        'description': 'normal test',
        'input': "/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash/../../../../../..",
        'output': "/",
        'active': True
    },
    'test_case_5': {
        'description': 'normal test',
        'input': "/",
        'output': "/",
        'active': True
    },
    'test_case_4': {
        'description': 'normal test',
        'input': "abc/foo/bar/baz/../../..",
        'output': "abc",
        'active': True
    },
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = shortenPath(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
