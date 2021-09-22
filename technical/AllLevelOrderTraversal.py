class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []

        if not root:
            return levels

        queue = []
        queue.append(root)

        while queue:

            level = []

            for _ in range(len(queue)):

                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return levels
