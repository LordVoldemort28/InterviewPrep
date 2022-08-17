class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = {}

        if not root:
            return levels

        queue = []
        queue.append(root)
        
        currentLevel = 1
        while queue:

            level = []

            for _ in range(len(queue)):

                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels[currentLevel] = level
            currentLevel += 1
        return levels

class TreeNode:
    
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None
        
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

tool = Solution()
print(tool.levelOrder(root))
