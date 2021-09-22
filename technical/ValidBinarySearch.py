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


def inorder(root, values):

    if root:

        inorder(root.left, values)
        values.append(root.value)
        inorder(root.right, values)

    return values


def is_binary_search_tree(root):

    # Determine if the tree is a valid binary search tree
    values = inorder(root, [])

    for idx in range(0, len(values)-1):
        if values[idx] > values[idx+1]:
            return False

    return True


#=========Test 1===============
tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)

print(is_binary_search_tree(tree))

#=========Test 2===============
tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(80)
left.insert_left(20)
left.insert_right(60)
right.insert_left(70)
right.insert_right(90)

print(is_binary_search_tree(tree))
