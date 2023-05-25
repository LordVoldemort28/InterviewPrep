class Stack():

    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.stack:
            return None

        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def isEmpty(self):
        if not self.stack:
            return True

        return False

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]
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
maxStack.push(9)
maxStack.push(7)
maxStack.push(7)
maxStack.push(8)

print(maxStack.get_max())

maxStack.pop()

print(maxStack.get_max())
