def reverse(chars, left, right):

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return chars


def reverse_sentence(chars):

    reverse(chars, 0, len(chars)-1)
    start_index = 0

    for i in range(0, len(chars)+1):

        if i == len(chars) or chars[i] == ' ':
            reverse(chars, start_index, i-1)
            start_index = i+1

    return chars


message = list('one another get')
print(reverse_sentence(message))
