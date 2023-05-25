class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = []
        self.readTree(root)

    def readTree(self, root):

        if not root:
            return

        self.readTree(root.left)
        self.queue.append(root.val)
        self.readTree(root.right)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) != 0


class BSTIterator2(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = []
        self.readTree(root)

    def readTree(self, root):

        while root is not None:
            self.queue.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        item = self.queue.pop()
        self.readTree(item.right)
        return item.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue
