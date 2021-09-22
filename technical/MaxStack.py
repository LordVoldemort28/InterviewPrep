class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


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
