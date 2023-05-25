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
    

class Solution(object):
    def isValid(self, s):
        openers_to_closers = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        opening = openers_to_closers.values()
        closing = openers_to_closers.keys()

        stack = Stack()

        for bracket in s:

            if bracket in opening:
                stack.push(bracket)
            elif bracket in closing and stack.peek() is openers_to_closers[bracket]:
                stack.pop()
            else:
                return False

        if stack.peek() is None:
            return True

        return False

print(Solution().isValid('()'))
print(Solution().isValid('([]{[]})[]{{}()}'))
print(Solution().isValid('([)]'))
