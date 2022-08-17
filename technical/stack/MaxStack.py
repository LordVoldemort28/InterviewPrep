import __init__
from dsa.stack.Stack import SimpleStack as Stack
class MaxStack(object):

    # Implement the push, pop, and get_max methods

    def __init__(self):
        self.stack = Stack()
        self.max_element_stack = Stack()

    def push(self, item):

        self.stack.push(item)

        if self.max_element_stack.peek() is None or self.max_element_stack.peek() <= item:
            self.max_element_stack.push(item)

    def pop(self):

        ele = self.stack.pop()

        if ele == self.max_element_stack.peek():
            self.max_element_stack.pop()

        return ele

    def get_max(self):

        return self.max_element_stack.peek()


maxStack = MaxStack()

maxStack.push(5)

maxStack.push(4)
maxStack.push(7)
maxStack.push(7)
maxStack.push(8)

print(maxStack.get_max())

maxStack.pop()

maxStack.get_max()
