class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:

    def serialize(self, root):
        
        stack = [root]
        result = []
        while stack:
            current = stack.pop()
            
            if not current:
                result.append('N')
                continue
            
            result.append(str(current.val))
            stack.append(current.right)
            stack.append(current.left)

        return ",".join(result)
    
    def deserialize(self, order):
        values = order.split(',')
        self.counter = 0
        
        def dfs():
            
            if values[self.counter] == 'N':
                self.counter += 1
                return None
            
            node = TreeNode(int(values[self.counter]))
            self.counter += 1
            
            node.left = dfs()
            node.right = dfs()
            
            return node

        return dfs()
    
tree = Tree()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

encrypt = tree.serialize(root)
print(encrypt)
print(tree.deserialize(encrypt))
