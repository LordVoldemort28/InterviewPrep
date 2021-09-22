class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None

        return self.queue.pop(0)

    def is_empty(self):
        if not self.queue:
            return True

        return False


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


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def bfs_traverse(self, root):

        queue = Queue()
        queue.enqueue(root)
        while not queue.is_empty():

            current = queue.dequeue()
            print(current.value)

            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)

    def dfs_traverse(self, root):

        stack = Stack()
        stack.push(root)
        while stack.peek():

            current = stack.pop()
            print(current.value)

            if current.right:
                stack.push(current.right)

            if current.left:
                stack.push(current.left)


tree = BinaryTreeNode(5)
left = tree.insert_left(8)
right = tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right.insert_right(4)

tree.dfs_traverse(tree)
