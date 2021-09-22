def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    char_count = [0] * 128

    for word in the_string:
        char_count[ord(word)] += 1

    odd_count = 0
    for count in char_count:
        if count % 2 == 1:
            odd_count += 1

        if odd_count > 1:
            return False

    return True


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    unpaired_word = set()

    for word in the_string:

        if word in unpaired_word:
            unpaired_word.remove(word)
        else:
            unpaired_word.add(word)
    return len(unpaired_word) > 1


result = has_palindrome_permutation('aabcbcd')
print(result)

result = has_palindrome_permutation('aabbcd')
print(result)
