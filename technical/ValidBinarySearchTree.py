# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n)time and O(d) space
def validateBst(tree, minValue=float("-inf"), maxValue=float("inf")):

	if not tree:
		return True

	if not(minValue <= tree.value < maxValue):
		return False

	return (validateBst(tree.left, minValue, tree.value) and
        validateBst(tree.right, tree.value, maxValue))


