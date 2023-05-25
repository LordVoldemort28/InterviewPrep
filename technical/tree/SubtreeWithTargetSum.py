class TreeNode:
    
    def __init__(self, value):
        self.value = value;
        self.left = None
        self.right = None
        
class Solution():
    
    def subtreeWithTargetSum(self, root, target):
        
        self.exist = False
        
        def search(root):
        
            if not root:
                return 0
            
            left = search(root.left)
            right = search(root.right)
            
            sum = left + right + root.value
            
            if sum == target:
                self.exist = True
            
            return sum
        
        search(root)
        return self.exist
    
# Driver Code
if __name__ == '__main__':

    root = TreeNode(8)
    root.left = TreeNode(5)
    root.right = TreeNode(4)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(12)
    root.left.right.right.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.right.right.left = TreeNode(3)
    sum = 22

if (Solution().subtreeWithTargetSum(root, sum)) :
    print("Yes" )
else:
    print("No")
