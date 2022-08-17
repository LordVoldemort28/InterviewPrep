import __init__
from dsa.stack.Stack import SimpleStack

def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    stack = SimpleStack()

    count = 0

    for idx in range(opening_paren_index, len(sentence)):

        if sentence[idx] == '(':
            stack.push(sentence[idx])
        else:
            stack.pop()

        if stack.peek() == None:
            return count + opening_paren_index

        count += 1

    return -1


print(get_closing_paren('((((()))))', 2))
