class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):

        self.diameter = float('-inf')

        def findDiameter(treeNode):

            if not treeNode:
                return 0

            left = findDiameter(treeNode.left)
            right = findDiameter(treeNode.right)

            self.diameter = max(self.diameter, (left+right))

            return max(left, right) + 1

        findDiameter(root)

        return self.diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(root))
