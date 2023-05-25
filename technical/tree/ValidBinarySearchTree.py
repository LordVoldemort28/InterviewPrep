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


def inOrder(root, values):

    if root:

        inOrder(root.left, values)
        values.append(root.value)
        inOrder(root.right, values)

    return values


# O(n)time and O(d) space
def validateBst(node, minValue=float("-inf"), maxValue=float("inf")):

	if not node:
		return True

	if not(minValue <= node.value < maxValue):
		return False

	return (validateBst(node.left, minValue, node.value) and
            validateBst(node.right, node.value, maxValue))


#=========Test 1===============
tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)

print(validateBst(tree))

#=========Test 2===============
tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(80)
left.insert_left(20)
left.insert_right(60)
right.insert_left(70)
right.insert_right(90)

print(validateBst(tree))
