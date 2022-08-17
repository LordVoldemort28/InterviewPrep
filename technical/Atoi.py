def atoi(string):
    
    number = 0
    digitPlaces = 0
    
    #reverse iteration
    for idx in reversed(range(len(string))):
        
        #Ignore spaces
        if string[idx] == " ":
            continue
        
        #If character is dash then convert number to negative
        if string[idx] == "-":
            number *= -1
            continue
        
        #Non number character
        if ord(string[idx]) not in range(48, 58):
            continue
    
        number += int(string[idx]) * pow(10, digitPlaces)
        digitPlaces += 1
        
    return number
    
print(atoi("23456"))
print(atoi("0"))
print(atoi("   -(-42)"))
print(atoi("4193 with words"))
print(atoi("-4193 with words"))
