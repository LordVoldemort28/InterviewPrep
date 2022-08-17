def minHeightBst(arr):
    return midTraversal(arr, 0, len(arr)-1)

def midTraversal(arr, low, high, root=None):

    if low <= high:

        mid = (low+high)//2

        if root:
            root.insert(arr[mid])
        else:
            root = BST(arr[mid])

        midTraversal(arr, low, mid-1, root)
        midTraversal(arr, mid+1, high, root)

    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def getTreeHeight(self, tree, height=0):
        if tree is None:
            return height
        leftTreeHeight = self.getTreeHeight(tree.left, height + 1)
        rightTreeHeight = self.getTreeHeight(tree.right, height + 1)
        return max(leftTreeHeight, rightTreeHeight)


bst = minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22])

print(bst.getTreeHeight(bst) == 4)

