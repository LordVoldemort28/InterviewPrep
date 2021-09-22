class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None

        return self.queue.pop(0)

    def is_empty(self):
        if not self.queue:
            return True

        return False


class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):

        if not self.stack:
            return None

        return self.stack.pop()

    def peek(self):

        if not self.stack:
            return None

        return self.stack[-1]
    
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BasicTree():
    def __init__(self):
        return
    
    def isTreeEmpty(self, root):
        if root == None:
            return True
        return False
    
    def isTreeFull(self, root):
        
        if not self.isTreeEmpty(root):
            return True
        
        if root.left is not None and root.right is not None:
            return True
        

    def inOrder(self, root):
        """
        Visit left->Node->Right
        Use Case: InOrder traversal gives nodes in non-decreasing order. 
        To get nodes of BST in non-increasing order, a variation of 
        InOrder traversal where InOrder traversal s reversed can be used. 
        """
        if root:
            self.inOrder(root.left)
            print(root.value, end=", ")
            self.inOrder(root.right)

    def postOrder(self, root):
        """
        Visit left->right->Node
        Use case: Postorder traversal is used to delete the tree
        """
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value, end=", ")

    def preOrder(self, root):
        """
        Visit Node->left->right 
        Use case: Preorder traversal is used to create a copy of the tree
        """
        if root:
            print(root.value, end=", ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def bfs_traverse(self, root):
        """
        Print all nodes level wise
        """
        queue = Queue()
        queue.enqueue(root)
        while not queue.is_empty():

            current = queue.dequeue()
            print(current.value)

            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)

    def dfs_traverse(self, root):
        """
        In general InOrder, PreOrder and PostOrder all are DFS traversal.
        And this traversal is same as PreOrder
        """
        stack = Stack()
        stack.push(root)
        while stack.peek():

            current = stack.pop()
            print(current.value)

            if current.right:
                stack.push(current.right)

            if current.left:
                stack.push(current.left)

def main():
    tree = BasicTree()

    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)

    print("In order traversal: ", end="")
    tree.inOrder(root)
    print()
    
    print("Post order traversal: ", end="")
    tree.postOrder(root)
    print()
    
    print("Pre order traversal: ", end="")
    tree.preOrder(root)
    print()
    
    print("BFS traversal: ", end="")
    tree.bfs_traverse(root)
    print()
    
    print("DFS traversal: ", end="")
    tree.dfs_traverse(root)
    print()
    return

if __name__ == '__main__':
    main()
