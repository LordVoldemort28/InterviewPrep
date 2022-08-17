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


def is_balanced_binary_tree(root):

    stack = Stack()
    max_depth = float("-inf")
    min_depth = float("inf")

    stack.push((root, 0))

    while stack.peek():

        current, depth = stack.pop()

        if (not current.left) and (not current.right):
            max_depth = max(depth, max_depth)
            min_depth = min(depth, min_depth)

        if max_depth - min_depth > 1:
            return False

        if current.left:
            stack.push((current.left, (depth+1)))

        if current.right:
            stack.push((current.right, (depth+1)))

    return True


tree = BinaryTreeNode(5)
left = tree.insert_left(8)
right = tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right.insert_right(4)
result = is_balanced_binary_tree(tree)

print(result)


