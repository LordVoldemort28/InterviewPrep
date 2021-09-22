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


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):

        while self.stack1.peek():
            value = self.stack1.pop()
            self.stack2.push(value)

        self.stack2.pop()

        while self.stack2.peek():
            self.stack1.push(self.stack2.pop())

        return value


queue = QueueTwoStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.dequeue()
actual = queue.dequeue()
actual = queue.dequeue()
print(actual)
