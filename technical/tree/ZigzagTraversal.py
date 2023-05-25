from collections import defaultdict


class Solution(object):
    def zigzagLevelOrder(self, root):
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
            
            if level % 2 == 0:
                levels[level].insert(0, node.val)
            else:
                levels[level].append(node.val)

            queue.append((node.left, (level+1)))
            queue.append((node.right, (level+1)))

        return [levelValues for levelValues in levels.values()]
