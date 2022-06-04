def caesarCipherEncryptor(string, key):
    #97-122
    out = ''
    for char in string:

      out += chr((((ord(char)-97)+key) % 26) + 97)

    return out


test_cases = {
    'test_case_1': {
        'description': 'big test',
        'input': {
            'string': 'ovmqkwtujqmfkao',
            'key': 52
        },
        'output': 'ovmqkwtujqmfkao',
        'active': True
    },
    'test_case_2': {
        'description': 'normal test',
        'input': {
            'string': 'xyz',
            'key': 2
        },
        'output': 'zab',
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
      print('Skipped!')
      continue

    input = data['input']
    result = caesarCipherEncryptor(input['string'], input['key'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
