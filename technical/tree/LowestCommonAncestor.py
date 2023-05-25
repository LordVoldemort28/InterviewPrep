# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __lt__(self, node):
        return self.val < node.val

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        stack = [root]
        parents = {root: None}
        
        while p not in parents or q not in parents:
            
            node = stack.pop()
            
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            
            if node.right:
                parents[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        while q not in ancestors:
            q = parents[q]
        return q

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(1)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
print(Solution().lowestCommonAncestor(root, root.left, root.left.right.right).val)
print(Solution().lowestCommonAncestor(
    root, root.left, root.right).val)
