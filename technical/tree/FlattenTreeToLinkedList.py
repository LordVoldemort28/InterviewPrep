class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        
        if not root:
            return 
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
        
        return root
        
    def flattenLeftSide(self, root):
        """
        Flattening from left side
        """
        if not root:
            return
        
        self.flatten(root.left)
        
        if root.left:
            
            if root.right:
                temp = root.right
                
                endLeftRight = root.left
                
                while endLeftRight.right:
                    
                    endLeftRight = endLeftRight.right
                
                endLeftRight.right = temp
            root.right = root.left
            root.left = None
            
        self.flatten(root.right)
        
        return root
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.left.right = TreeNode(6.6)

modified = Solution().flatten(root)

while modified:
    
    print(modified.val)
    modified = modified.right
