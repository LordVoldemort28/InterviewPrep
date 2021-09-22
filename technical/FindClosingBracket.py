class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):

        if not self.stack:
            return None

        return self.stack.pop()

    def peek(self):

        if not self.stack:
            return None

        return self.stack[-1]


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    stack = Stack()

    count = 0

    for idx in range(opening_paren_index, len(sentence)):

        if sentence[idx] is '(':
            stack.push(sentence[idx])
        else:
            stack.pop()

        if stack.peek() is None:
            return count + opening_paren_index

        count += 1

    return -1


print(get_closing_paren('((((()))))', 2))
