def reverse(chars):

    mid = len(chars)//2
    size = len(chars) - 1
    for i in range(0, mid):
        chars[i], chars[size-i] = chars[size-i], chars[i]
    return chars

#OR


def reverse_while(chars):

    left, right = 0, len(chars)-1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return chars


list_of_chars = ['A', 'B', 'C', 'D', 'E', 'F']
print(reverse_while(list_of_chars))
