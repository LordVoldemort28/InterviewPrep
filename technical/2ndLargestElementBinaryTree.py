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


def find_largest_value(root, prev=float("-inf")):

    if root.left:
        return find_largest_value(root.left, prev)

    if root:
        return root.value

    if root.right:
        return find_largest_value(root.right, prev)


tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)

print(find_largest_value(tree))


##Test 2
tree = BinaryTreeNode(50)
tree.insert_left(30)

print(find_largest_value(tree))
