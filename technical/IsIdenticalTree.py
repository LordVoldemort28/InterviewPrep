'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return true/false or 1/0


def inorder(root, traversal):
    if root:
        inorder(root.left, traversal)
        traversal.append(root.data)
        inorder(root.right, traversal)

    return traversal


def isIdentical(root1, root2):
    # Code here
    return inorder(root1, []) == inorder(root2, [])


# ========================================================

def isIdentical(root1, root2):
    # Code here
    if ((root1 is None and root2 is not None) or (root2 is None and root1 is not None)):
        return False

    if (root1 is None and root2 is None):
        return True

    if (root1.data != root2.data):
        return False

    if (root1.data == root2.data):
        return True and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
