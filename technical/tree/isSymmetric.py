class Solution(object):
    def isSymmetricRecursive(self, root):

        def isSys(L, R):
            if L and R and L.val == R.val:
                return isSys(L.right, R.left) and isSys(L.left, R.right)
            return L == R

        return isSys(root.left, root.right)

    def isSymmetricIterative(self, root):
        
        if not root:
            return False
        
        queue = [(root.left, root.right)]
        
        while queue:
            
            L, R = queue.pop(0)
            
            if not L and not R:
                continue
            
            if not L or not R or (L.val != R.val):
                return False

            queue.append((L.right, R.left))
            queue.append((L.left, R.right))
                
        return True
    

class BinaryTreeNode(object):

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


# tree = BinaryTreeNode(1)
# left = tree.insert_left(2)
# right = tree.insert_right(2)
# left.insert_left(3)
# left.insert_right(4)
# right.insert_left(4)
# right.insert_right(3)

# print("Is symmetric: {}".format(Solution().isSymmetricIterative(tree)))
# print("Expected is: {}".format(True))

tree = BinaryTreeNode(1)
left = tree.insert_left(2)
right = tree.insert_right(2)
left.insert_left(3)
right.insert_left(3)

print("Is symmetric: {}".format(Solution().isSymmetricIterative(tree)))
print("Expected is: {}".format(True))

print("Is symmetric: {}".format(Solution().isSymmetricIterative(tree)))
print("Expected is: {}".format(False))
