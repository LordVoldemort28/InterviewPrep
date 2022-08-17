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


def is_valid(code):

    openers_to_closers = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    opening = openers_to_closers.values()
    closing = openers_to_closers.keys()

    stack = Stack()

    for bracket in code:

        if bracket in opening:
            stack.push(bracket)
        elif bracket in closing and stack.peek() is openers_to_closers[bracket]:
            stack.pop()
        else:
            return False

    if stack.peek() is None:
        return True

    return False


print(is_valid('()'))
print(is_valid('([]{[]})[]{{}()}'))
print(is_valid('([)]'))
