class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    stack = [tree]
    visited = []
    count = 1
    
    while stack:

        current = stack[-1]

        if current.right and (current.right not in visited):
            current = current.right
            stack.append(current)
            continue

        result = stack.pop()

        if count == k:
            return result.value

        visited.append(result)
        count += 1

        if current.left and (current.left not in visited):
            current = current.left
            stack.append(current)

    return None

root = BST(4)
root.left = BST(2)
root.right = BST(7)
root.left.left = BST(1)
root.left.right = BST(3)
root.right.left = BST(6)
root.right.right = BST(9)

print(findKthLargestValueInBst(root, 3) == 6)

