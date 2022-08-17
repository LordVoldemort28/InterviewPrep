def isValidIPDigit(string):
    if len(string) > 1 and string[0] == '0':
        return False
    stringAsInt = int(string)
    return stringAsInt >= 0 and stringAsInt <= 255

def validIPAddresses(string):
    
    if len(string) < 4 or len(string) > 12:
        return []
    
    nChars = len(string)
    validIpAddressFound = []
    
    for i in range(1, min(nChars, 4)):
        
        currentIPAddress = ['', '', '', '']
        
        currentIPAddress[0] = string[:i]
        if not isValidIPDigit(currentIPAddress[0]):
            continue
        
        for j in range((i+1), i + min((nChars-i), 4)):
            
            currentIPAddress[1] = string[i:j]
            if not isValidIPDigit(currentIPAddress[1]):
                continue
            
            for k in range((j+1), j +min((nChars-j), 4)):
                
                currentIPAddress[2] = string[j:k]
                currentIPAddress[3] = string[k:]
                
                if not isValidIPDigit(currentIPAddress[2]) or not isValidIPDigit(currentIPAddress[3]):
                    continue
                
                validIpAddressFound.append('.'.join(currentIPAddress))
                
    return validIpAddressFound

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': "1921680",
        'output': ['1.9.216.80', '1.92.16.80', '1.92.168.0', '19.2.16.80', '19.2.168.0', '19.21.6.80', '19.21.68.0', '19.216.8.0', '192.1.6.80', '192.1.68.0', '192.16.8.0'],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = validIPAddresses(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
