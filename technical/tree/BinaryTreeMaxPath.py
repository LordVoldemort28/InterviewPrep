class Solution(object):
    def maxPathSum(self, root):
        
        self.maxSum = float("-inf")
        
        def util(root):
                
            if not root:
                return 0
            
            #Comparing with zero to drop -ve sum
            left = max(0, util(root.left))
            right = max(0, util(root.right))
            
            self.maxSum = max(self.maxSum, (root.val+left+right))

            return root.val + max(left, right)
        
        util(root)
        
        return self.maxSum
