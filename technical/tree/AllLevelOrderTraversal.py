from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        levels = defaultdict(list)

        queue = [(root, 1)]

        while queue:

            node, level = queue.pop(0)

            if not node:
                continue

            levels[level].append(node.val)

            queue.append((node.left, (level+1)))
            queue.append((node.right, (level+1)))

        return [levelValues for levelValues in levels.values()]

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
# root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

tool = Solution()
print(tool.levelOrder(root))

